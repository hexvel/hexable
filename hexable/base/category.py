import abc
import typing

from hexable.types.hexable_types.base_model import BaseModel

if typing.TYPE_CHECKING:
    from hexable.api import API

T = typing.TypeVar("T", bound=BaseModel)


class BaseCategory(abc.ABC):
    def __init__(self, api: "API") -> None:
        self._api = api

    @classmethod
    def get_params_from_locals(
        cls, params: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        return {k: v for k, v in params.items() if k != "self" and v is not None}
