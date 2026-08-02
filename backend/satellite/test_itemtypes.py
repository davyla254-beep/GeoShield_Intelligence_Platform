import asyncio

from planet import Session, Auth
from planet.clients import DataClient

from backend.satellite.auth import get_planet_key


async def main():

    auth = Auth.from_key(get_planet_key())

    async with Session(auth=auth) as sess:

        client = DataClient(sess)

        print(await client.get_item("PSScene", "20260726_175350_76_254f"))


asyncio.run(main())