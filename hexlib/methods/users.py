import typing

from hexlib.base.category import BaseCategory
from hexlib.models.users import UsersGet

if typing.TYPE_CHECKING:
    from hexlib.api import API


class Users(BaseCategory):
    def __init__(self, api: "API") -> None:
        self._api = api

    async def get(
        self,
        user_ids: typing.Optional[list[int]] | typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        name_case: typing.Optional[str] = None,
        from_group_id: typing.Optional[int] = None,
    ) -> list[UsersGet]:
        params = self.get_params_from_locals(locals())
        response = await self._api.method("users.get", **params)
        users_get_list = [UsersGet(**user) for user in response]
        return users_get_list

    async def get_followers(
        self, user_id: int, offset: int = 0, count: int = 100, fields: str = ""
    ) -> list[dict]:
        params = self.get_params_from_locals(locals())
        return await self._api.method("users.getFollowers", **params)

    async def get_subscriptions(
        self,
        user_id: int,
        extended: typing.Optional[int] = 0,
        offset: typing.Optional[int] = 0,
        count: int = 100,
        fields: typing.Optional[str] = "",
    ) -> list[dict]:
        params = self.get_params_from_locals(locals())
        return await self._api.method("users.getSubscriptions", **params)

    async def report(
        self,
        user_id: int,
        type: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
    ) -> bool:
        params = self.get_params_from_locals(locals())
        return await self._api.method("users.report", **params)

    async def search(
        self,
        age_from: typing.Optional[int] = None,
        age_to: typing.Optional[int] = None,
        birth_day: typing.Optional[int] = None,
        birth_month: typing.Optional[int] = None,
        birth_year: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        company: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        country_id: typing.Optional[int] = None,
        fields: typing.Optional[list] = None,
        from_group_id: typing.Optional[int] = None,
        from_list: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        has_photo: typing.Optional[bool] = None,
        hometown: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        online: typing.Optional[bool] = None,
        position: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        religion: typing.Optional[str] = None,
        school: typing.Optional[int] = None,
        school_city: typing.Optional[int] = None,
        school_class: typing.Optional[int] = None,
        school_country: typing.Optional[int] = None,
        school_year: typing.Optional[int] = None,
        screen_ref: typing.Optional[str] = None,
        sex: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        university: typing.Optional[int] = None,
        university_chair: typing.Optional[int] = None,
        university_country: typing.Optional[int] = None,
        university_faculty: typing.Optional[int] = None,
        university_year: typing.Optional[int] = None,
    ) -> typing.List[str]:
        params = self.get_params_from_locals(locals())
        return await self._api.method("users.search", **params)
