from aiohttp import ClientSession
from ujson import dumps


async def main():
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url=
        )