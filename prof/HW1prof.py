from aiohttp import ClientSession
from ujson import dumps
import asyncio

async def main():
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url=api/address/1wiz18xYmhRX6xStj2b9t1rwWX4GKUgpv
        )
        print(response)


asyncio.run(main())