import abc
import typing

if typing.TYPE_CHECKING:
    from hexlib.api import API


class BaseCategory(abc.ABC):
    def __init__(self, api: "API") -> None:
        self._api = api

    @classmethod
    def get_params_from_locals(
        cls, params: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        exclude_params = params.copy()
        return {
            k[1:] if k.startswith("_") else k: int(v) if isinstance(v, bool) else v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }
