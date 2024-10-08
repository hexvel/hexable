import typing

from typing_extensions import Literal

from hexable.types.hexable_types.codegen.methods.video import \
    VideoCategory  # type: ignore
from hexable.types.hexable_types.codegen.responses.base import (
    BaseOkResponse, BaseOkResponseModel)
from hexable.types.hexable_types.codegen.responses.video import \
    VideoChangeVideoAlbumsResponse


class VideoCategory(VideoCategory):
    @typing.overload
    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = ...,
        album_ids: typing.Optional[Literal[None]] = None,
        **kwargs,
    ) -> BaseOkResponseModel: ...

    @typing.overload
    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[Literal[None]] = None,
        album_ids: typing.Optional[typing.List[int]] = ...,
        **kwargs,
    ) -> typing.List[int]: ...

    async def add_to_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> typing.Union[BaseOkResponseModel, typing.List[int]]:
        """video.addToAlbum method

        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.method("video.addToAlbum", params)
        model = self.get_model(
            ((("album_ids",), VideoChangeVideoAlbumsResponse),),
            default=BaseOkResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = ...,
        album_ids: typing.Optional[Literal[None]] = None,
        **kwargs,
    ) -> BaseOkResponseModel: ...

    @typing.overload
    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[Literal[None]] = None,
        album_ids: typing.Optional[typing.List[int]] = ...,
        **kwargs,
    ) -> typing.List[int]: ...

    async def remove_from_album(
        self,
        owner_id: int,
        video_id: int,
        target_id: typing.Optional[int] = None,
        album_id: typing.Optional[int] = None,
        album_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> typing.Union[BaseOkResponseModel, typing.List[int]]:
        """video.removeFromAlbum method

        :param owner_id:
        :param video_id:
        :param target_id:
        :param album_id:
        :param album_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.method("video.removeFromAlbum", params)
        model = self.get_model(
            ((("album_ids",), VideoChangeVideoAlbumsResponse),),
            default=BaseOkResponse,
            params=params,
        )
        return model(**response).response


__all__ = ("VideoCategory",)