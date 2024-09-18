import typing

from hexable.base.category import BaseCategory
from hexable.models.users import UsersGet, UsersGetSubscriptions, UsersItem

if typing.TYPE_CHECKING:
    from hexable.api import API


class Users(BaseCategory):
    def __init__(self, api: "API") -> None:
        super().__init__(api)
        self._api = api

    async def get(
        self,
        user_ids: typing.Optional[list[int]] | typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        name_case: typing.Optional[str] = None,
        from_group_id: typing.Optional[int] = None,
    ) -> list["UsersGet"]:
        params = self.get_params_from_locals(locals())

        response = await self._api.method("users.get", **params)
        return [UsersGet(**item) for item in response]

    async def get_followers(
        self,
        user_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
    ) -> "UsersItem":
        params = self.get_params_from_locals(locals())

        response = await self._api.method("users.getFollowers", **params)
        return UsersItem(**response)

    async def get_subscriptions(
        self,
        user_id: int,
        extended: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
    ) -> "UsersGetSubscriptions":
        params = self.get_params_from_locals(locals())

        response = await self._api.method("users.getSubscriptions", **params)
        return UsersGetSubscriptions(**response)

    async def report(
        self,
        user_id: int,
        type: typing.Literal["porn", "spam", "insult", "advertisement"] = None,
        comment: typing.Optional[str] = None,
    ) -> int:
        params = self.get_params_from_locals(locals())

        response = self._api.method("users.report", **params)
        return response

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
    ) -> "UsersItem":
        params = self.get_params_from_locals(locals())

        response = await self._api.method("users.search", **params)
        return UsersItem(**response)
