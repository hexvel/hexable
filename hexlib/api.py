import asyncio
import enum
import re
import time
import typing

import aiohttp
from loguru import logger
from pydantic import BaseModel

from hexlib.base.api_serialize import APISerializableMixin
from hexlib.base.json_parser import BaseJSONParser
from hexlib.base.pages import User
from hexlib.base.session_container import SessionContainerMixin
from hexlib.exceptions import APIError
from hexlib.json_parsers import json_parser_policy
from hexlib.methods.users import Users
from hexlib.pretty_view import pretty_view


@enum.unique
class OwnerType(enum.Enum):
    USER = enum.auto()
    GROUP = enum.auto()
    NOBODY = enum.auto()


class APIResponse(BaseModel):
    response: typing.Optional[typing.Any] = None
    error: typing.Optional[dict] = None


class API(SessionContainerMixin):
    def __init__(
        self,
        token: str,
        version: str = "5.199",
        url: str = "https://api.vk.com/method/",
        requests_session: typing.Optional[aiohttp.ClientSession] = None,
        json_parser: typing.Optional[BaseJSONParser] = None,
    ) -> None:
        SessionContainerMixin.__init__(
            self, requests_session=requests_session, json_parser=json_parser
        )

        self._token = token
        self._version = version
        self._url = url
        self._owner_schema: typing.Optional[typing.Union[User]] = None
        self._owner_type: OwnerType = OwnerType.NOBODY

        self._method_name = ""
        self._requests_delay = 1 / 20
        self._last_request_timestamp = 0.0

        self._stable_request_params = {
            "access_token": self._token,
            "v": self._version,
        }

    @property
    def users(self) -> "Users":
        return Users(self)

    async def determine_the_type_of_owner(self):
        if self._owner_type != OwnerType.NOBODY and self._owner_schema is not None:
            return self._owner_type, self._owner_schema
        owner_schema = await self.method("users.get")
        if owner_schema:
            self._owner_schema = User(owner_schema[0])
            self._owner_type = OwnerType.USER
        # else:
        #     owner_schema = await self.use_cache().method("groups.get_by_id")
        #     self._owner_schema = Group(owner_schema[0])
        #     self._owner_type = OwnerType.GROUP

        self._update_requests_delay()
        return self._owner_type, self._owner_schema

    def _update_requests_delay(self) -> None:
        if self._token in {OwnerType.USER, OwnerType.NOBODY}:
            self._requests_delay = 1 / 3
        else:
            self._requests_delay = 1 / 20

    async def method(self, method_name: str, **request_params) -> typing.Any:
        return await self._make_api_request(
            method_name=method_name, request_params=request_params
        )

    async def _make_api_request(
        self, method_name: str, request_params: typing.Dict[str, typing.Any]
    ) -> typing.Any:
        real_method_name = _convert_method_name(method_name)
        real_request_params = _convert_params_for_api(request_params)
        extra_request_params = self._stable_request_params.copy()
        extra_request_params.update(real_request_params)

        api_request_delay = self._get_waiting_time()
        await asyncio.sleep(api_request_delay)

        response = await self._send_api_request(real_method_name, extra_request_params)
        response = APIResponse.model_validate(response)
        logger.debug("Response is: {response}", response=pretty_view(response.response))

        if "error" in response:
            await self.close_session()
            error = response.error.copy()
            exception_class = APIError[error["error_code"]][0]
            raise exception_class(
                status_code=error.pop("error_code"),
                description=error.pop("error_msg"),
                request_params=error.pop("request_params"),
                extra_fields=error,
            )
        else:
            response = response.response
        return response

    async def _send_api_request(self, method_name: str, params: dict) -> typing.Any:
        while True:
            try:
                async with self.requests_session.post(
                    self._url + method_name, data=params
                ) as response:
                    response = await self.parse_json_body(response)
                    if "error" in response and response["error"]["error_code"] == 10:
                        logger.warning(
                            "VK Internal server error occured while calling {method_name} ({params}): {"
                            "error_message}. Retrying in 10 seconds...",
                            method_name=method_name,
                            params=params,
                            error_message=response["error"]["error_msg"],
                        )
                        await asyncio.sleep(10)
                    else:
                        return response
            except aiohttp.ClientResponseError as error:
                if error.status >= 500:
                    logger.warning(
                        "VK Internal server error occured while calling {method_name} ({params}): {error_message}. "
                        "Retrying in 10 seconds...",
                        method_name=method_name,
                        params=params,
                        error_message=response["error"]["error_msg"],
                    )
                    await asyncio.sleep(10)
                else:
                    raise error
            except aiohttp.ServerDisconnectedError:
                await self.refresh_session()

    def _get_waiting_time(self) -> float:
        now = time.time()
        diff = now - self._last_request_timestamp
        if diff < self._requests_delay:
            wait_time = self._requests_delay - diff
            self._last_request_timestamp += wait_time
            return wait_time
        else:
            self._last_request_timestamp = now
            return 0.0


def _upper_zero_group(match: typing.Match, /) -> str:
    return match.group("let").upper()


def _convert_method_name(name: str, /) -> str:
    return re.sub(r"_(?P<let>[a-z])", _upper_zero_group, name)


def _convert_param_value(value, /):
    if isinstance(value, (list, set, tuple)):
        updated_sequence = map(_convert_param_value, value)
        return ",".join(updated_sequence)

    elif isinstance(value, dict):
        return json_parser_policy.dumps(value)

    elif isinstance(value, bool):
        return int(value)

    elif isinstance(value, APISerializableMixin):
        new_value = value.represent_as_api_param()
        return _convert_param_value(new_value)

    else:
        return str(value)


def _convert_params_for_api(params: dict, /):
    updated_params = {
        key: _convert_param_value(value)
        for key, value in params.items()
        if value is not None
    }
    return updated_params
