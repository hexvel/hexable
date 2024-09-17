import typing

from pydantic import BaseModel


class CityModel(BaseModel):
    id: int
    title: str


class LastSeenModel(BaseModel):
    platform: typing.Optional[int] = None
    time: typing.Optional[int] = None


class PhotoSizeModel(BaseModel):
    height: typing.Optional[int] = None
    type: typing.Optional[str] = None
    width: typing.Optional[int] = None
    url: typing.Optional[str] = None


class PhotoModel(BaseModel):
    album_id: typing.Optional[int] = None
    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    sizes: typing.Optional[list[PhotoSizeModel]] = None
    square_crop: typing.Optional[str] = None
    text: typing.Optional[str] = None
    web_view_token: typing.Optional[str] = None
    has_tags: typing.Optional[bool] = None
    orig_photo: typing.Optional[PhotoSizeModel] = None


class CordinateModel(BaseModel):
    x: typing.Optional[float] = None
    y: typing.Optional[float] = None
    x2: typing.Optional[float] = None
    y2: typing.Optional[float] = None


class CropPhotoModel(BaseModel):
    photo: typing.Optional[PhotoModel] = None
    crop: typing.Optional[CordinateModel] = None
    rect: typing.Optional[CordinateModel] = None


class OccupationModel(BaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: typing.Optional[str] = None


class CareerModel(BaseModel):
    group_id: typing.Optional[int] = None


class LangsModel(BaseModel):
    id: typing.Optional[int] = None
    native_name: typing.Optional[str] = None


class PersonalModel(BaseModel):
    alcohol: typing.Optional[int] = None
    inspired_by: typing.Optional[str] = None
    langs: typing.Optional[list[str]] = None
    langs_full: typing.Optional[list[LangsModel]] = None
    life_main: typing.Optional[int] = None
    people_main: typing.Optional[int] = None
    political: typing.Optional[int] = None
    religion: typing.Optional[str] = None
    religion_id: typing.Optional[int] = None
    smoking: typing.Optional[int] = None


class SchoolModel(BaseModel):
    city: typing.Optional[int] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    type: typing.Optional[int] = None
    type_str: typing.Optional[str] = None
    year_from: typing.Optional[int] = None
    year_graduated: typing.Optional[int] = None
    year_to: typing.Optional[int] = None
    speciality: typing.Optional[str] = None


class UsersGet(BaseModel):
    id: typing.Optional[int] = None
    nickname: typing.Optional[str] = None
    domain: typing.Optional[str] = None
    bdate: typing.Optional[str] = None
    city: typing.Optional[CityModel] = None
    timezone: typing.Optional[float] = None
    photo_50: typing.Optional[str] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_200_orig: typing.Optional[str] = None
    photo_400_orig: typing.Optional[str] = None
    photo_max: typing.Optional[str] = None
    photo_max_orig: typing.Optional[str] = None
    photo_id: typing.Optional[str] = None
    has_photo: typing.Optional[typing.Literal[0, 1]] = None
    has_mobile: typing.Optional[typing.Literal[0, 1]] = None
    is_friend: typing.Optional[typing.Literal[0, 1]] = None
    can_post: typing.Optional[typing.Literal[0, 1]] = None
    can_see_all_posts: typing.Optional[typing.Literal[0, 1]] = None
    can_see_audio: typing.Optional[typing.Literal[0, 1]] = None
    interests: typing.Optional[str] = None
    books: typing.Optional[str] = None
    tv: typing.Optional[str] = None
    quotes: typing.Optional[str] = None
    about: typing.Optional[str] = None
    games: typing.Optional[str] = None
    movies: typing.Optional[str] = None
    activities: typing.Optional[str] = None
    music: typing.Optional[str] = None
    can_write_private_message: typing.Optional[typing.Literal[0, 1]] = None
    can_send_friend_request: typing.Optional[typing.Literal[0, 1]] = None
    can_be_invited_group: typing.Optional[bool] = None
    mobile_phone: typing.Optional[str] = None
    home_phone: typing.Optional[str] = None
    site: typing.Optional[str] = None
    status: typing.Optional[str] = None
    last_seen: typing.Optional[LastSeenModel] = None
    crop_photo: typing.Optional[CropPhotoModel] = None
    followers_count: typing.Optional[int] = None
    blacklisted: typing.Optional[int] = None
    blacklisted_by_me: typing.Optional[int] = None
    is_favorite: typing.Optional[int] = None
    is_hidden_from_feed: typing.Optional[int] = None
    common_count: typing.Optional[int] = None
    occupation: typing.Optional[OccupationModel] = None
    career: typing.Optional[list[CareerModel]] = None
    military: typing.Optional[list] = None
    university: typing.Optional[int] = None
    university_name: typing.Optional[str] = None
    faculty: typing.Optional[int] = None
    faculty_name: typing.Optional[str] = None
    graduation: typing.Optional[int] = None
    home_town: typing.Optional[str] = None
    relation: typing.Optional[int] = None
    personal: PersonalModel = None
    universities: typing.Optional[list] = None
    schools: typing.Optional[list[SchoolModel]] = None
    relatives: typing.Optional[list] = None
    is_verify: typing.Optional[bool] = None
    sex: typing.Optional[int] = None
    screen_name: typing.Optional[str] = None
    online: typing.Optional[int] = None
    verified: typing.Optional[int] = None
    friend_status: typing.Optional[int] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    can_access_closed: typing.Optional[bool] = None
    is_closed: typing.Optional[bool] = None
