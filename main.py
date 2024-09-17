import asyncio
import os

from dotenv import load_dotenv

from hexlib.api import API

load_dotenv()


async def main():
    api = API(token=os.getenv("TOKEN"))

    await api.users.search(company="Hexvel")
    await api.close_session()


if __name__ == "__main__":
    asyncio.run(main())
