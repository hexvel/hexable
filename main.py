import asyncio
import os

from dotenv import load_dotenv
from loguru import logger

from hexable.api import API

logger.disable("hexable")

load_dotenv()


async def main():
    api = API(token=os.getenv("TOKEN"))

    res = await api.users.get_subscriptions(user_id=715616525)

    logger.debug(res)

    for r in res.users.items:
        print(r)

    await api.close_session()


if __name__ == "__main__":
    asyncio.run(main())
