import typing

from hexable.types.hexable_types.base_model import BaseModel, Field
from hexable.types.hexable_types.objects import SearchHint
from hexable.types.hexable_types.responses.base_response import BaseResponse


class SearchGetHintsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["SearchHint"] = Field()
    suggested_queries: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class SearchGetHintsResponse(BaseResponse):
    response: "SearchGetHintsResponseModel" = Field()
