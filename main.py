import asyncio

from hexlib.api import API


async def main():
    api = API("ваш токен сюда тык")

    await api.users.search(company="Hexvel")
    await api.close_session()


if __name__ == "__main__":
    asyncio.run(main())
