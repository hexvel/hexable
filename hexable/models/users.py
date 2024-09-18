from typing import List, Optional, Literal, Union

from pydantic import BaseModel


class CityModel(BaseModel):
    id: int
    title: str


class LastSeenModel(BaseModel):
    platform: Optional[int] = None
    time: Optional[int] = None


class PhotoSizeModel(BaseModel):
    height: Optional[int] = None
    type: Optional[str] = None
    width: Optional[int] = None
    url: Optional[str] = None


class PhotoModel(BaseModel):
    album_id: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    sizes: Optional[List[PhotoSizeModel]] = None
    square_crop: Optional[str] = None
    text: Optional[str] = None
    web_view_token: Optional[str] = None
    has_tags: Optional[bool] = None
    orig_photo: Optional[PhotoSizeModel] = None


class CoordinateModel(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None
    x2: Optional[float] = None
    y2: Optional[float] = None


class CropPhotoModel(BaseModel):
    photo: Optional[PhotoModel] = None
    crop: Optional[CoordinateModel] = None
    rect: Optional[CoordinateModel] = None


class OccupationModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class CareerModel(BaseModel):
    group_id: Optional[int] = None


class LangsModel(BaseModel):
    id: Optional[int] = None
    native_name: Optional[str] = None


class PersonalModel(BaseModel):
    alcohol: Optional[int] = None
    inspired_by: Optional[str] = None
    langs: Optional[List[str]] = None
    langs_full: Optional[List[LangsModel]] = None
    life_main: Optional[int] = None
    people_main: Optional[int] = None
    political: Optional[int] = None
    religion: Optional[str] = None
    religion_id: Optional[int] = None
    smoking: Optional[int] = None


class SchoolModel(BaseModel):
    city: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[int] = None
    type_str: Optional[str] = None
    year_from: Optional[int] = None
    year_graduated: Optional[int] = None
    year_to: Optional[int] = None
    speciality: Optional[str] = None


class UsersGet(BaseModel):
    id: Optional[int] = None
    nickname: Optional[str] = None
    domain: Optional[str] = None
    bdate: Optional[str] = None
    city: Optional[CityModel] = None
    timezone: Optional[float] = None
    track_code: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_200_orig: Optional[str] = None
    photo_400_orig: Optional[str] = None
    photo_max: Optional[str] = None
    photo_max_orig: Optional[str] = None
    photo_id: Optional[str] = None
    has_photo: Optional[Literal[0, 1]] = None
    has_mobile: Optional[Literal[0, 1]] = None
    is_friend: Optional[Literal[0, 1]] = None
    can_post: Optional[Literal[0, 1]] = None
    can_see_all_posts: Optional[Literal[0, 1]] = None
    can_see_audio: Optional[Literal[0, 1]] = None
    interests: Optional[str] = None
    books: Optional[str] = None
    tv: Optional[str] = None
    quotes: Optional[str] = None
    about: Optional[str] = None
    games: Optional[str] = None
    movies: Optional[str] = None
    activities: Optional[str] = None
    music: Optional[str] = None
    can_write_private_message: Optional[Literal[0, 1]] = None
    can_send_friend_request: Optional[Literal[0, 1]] = None
    can_be_invited_group: Optional[bool] = None
    mobile_phone: Optional[str] = None
    home_phone: Optional[str] = None
    site: Optional[str] = None
    status: Optional[str] = None
    last_seen: Optional[LastSeenModel] = None
    crop_photo: Optional[CropPhotoModel] = None
    followers_count: Optional[int] = None
    blacklisted: Optional[int] = None
    blacklisted_by_me: Optional[int] = None
    is_favorite: Optional[int] = None
    is_hidden_from_feed: Optional[int] = None
    common_count: Optional[int] = None
    occupation: Optional[OccupationModel] = None
    career: Optional[List[CareerModel]] = None
    military: Optional[List] = None
    university: Optional[int] = None
    university_name: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    home_town: Optional[str] = None
    relation: Optional[int] = None
    personal: Optional[PersonalModel] = None
    universities: Optional[List] = None
    schools: Optional[List[SchoolModel]] = None
    relatives: Optional[List] = None
    is_verify: Optional[bool] = None
    sex: Optional[int] = None
    screen_name: Optional[str] = None
    online: Optional[int] = None
    verified: Optional[int] = None
    friend_status: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    can_access_closed: Optional[bool] = None
    is_closed: Optional[bool] = None


class UsersItem(BaseModel):
    count: Optional[int] = None
    items: Optional[List[Union[UsersGet, int]]] = None


class UsersGetSubscriptions(BaseModel):
    users: Optional[UsersItem] = None
    groups: Optional[UsersItem] = None
