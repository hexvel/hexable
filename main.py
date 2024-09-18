import asyncio
import os

from dotenv import load_dotenv
from loguru import logger

from hexlib.api import API

load_dotenv()


async def main():
    api = API(token=os.getenv("TOKEN"))

    res = await api.users.get(
        user_ids=[733772362, 715616525],
        fields="activities,about,blacklisted,blacklisted_by_me,books,bdate,can_be_invited_group,can_post,"
               "can_see_all_posts,can_see_audio,can_send_friend_request,can_write_private_message,career,"
               "common_count,connections,contacts,city,crop_photo,domain,education,exports,followers_count,"
               "friend_status,has_photo,has_mobile,home_town,photo_100,photo_200,photo_200_orig,photo_400_orig,"
               "photo_50,sex,site,schools,screen_name,status,verified,games,interests,is_favorite,is_friend,"
               "is_hidden_from_feed,last_seen,maiden_name,military,movies,music,nickname,occupation,online,personal,"
               "photo_id,photo_max,photo_max_orig,quotes,relation,relatives,timezone,tv,universities,is_verified",
    )

    for i in res:
        logger.info(f"User: {i.id}, Name: {i.first_name} {i.last_name}")

    await api.close_session()


if __name__ == "__main__":
    asyncio.run(main())
