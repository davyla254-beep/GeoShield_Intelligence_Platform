import asyncio

from planet import Session, Auth
from planet.clients import DataClient

from backend.satellite.auth import get_planet_key

ITEM_ID = "20260726_181751_21_24d1"

async def main():
    auth = Auth.from_key(get_planet_key())

    async with Session(auth=auth) as sess:
        client = DataClient(sess)

        item = await client.get_item("PSScene", ITEM_ID)

        print("\nPERMISSIONS:\n")
        print(item["_permissions"])

asyncio.run(main())