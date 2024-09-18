import abc
import typing

from pydantic import BaseModel

if typing.TYPE_CHECKING:
    from hexable.api import API

T = typing.TypeVar("T", bound=BaseModel)


class BaseCategory(abc.ABC):
    def __init__(self, api: "API") -> None:
        self._api = api

    async def call_api_iter(
        self, method: str, model: typing.Type[T], **params
    ) -> typing.List[T]:
        response = await self._api.method(method, **params)
        return [model(**item) for item in response]

    async def call_api(self, method: str, model: typing.Type[T], **params) -> T:
        response = await self._api.method(method, **params)
        return model(**response)

    @classmethod
    def get_params_from_locals(
        cls, params: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        return {k: v for k, v in params.items() if k != "self" and v is not None}
