from __future__ import annotations

import dataclasses
import typing

import typing_extensions as tye

exceptions_storage: typing.Dict[int, typing.Type[APIError]] = {}


class _ParamsScheme(tye.TypedDict):
    key: str
    value: str


@dataclasses.dataclass
class APIError(Exception):
    description: str
    status_code: int
    request_params: typing.List[_ParamsScheme]
    extra_fields: dict

    def __class_getitem__(
            cls, code: typing.Union[int, typing.Tuple[int, Ellipsis]]
    ) -> typing.Tuple[typing.Type[APIError]]:
        result_classes = []
        codes = (code,) if isinstance(code, int) else code
        for code in codes:
            if code in exceptions_storage:
                result_classes.append(exceptions_storage[code])
            else:
                new_class = type(f"APIError [{code}]", (APIError,), {})
                new_class = typing.cast(typing.Type[APIError], new_class)
                exceptions_storage[code] = new_class
                result_classes.append(new_class)

        return tuple(result_classes)

    def __str__(self) -> str:
        return self.description

    def __repr__(self) -> str:
        return self.description
