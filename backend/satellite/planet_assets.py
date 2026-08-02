from planet import Session
from planet.clients import DataClient
from planet import Auth

from backend.satellite.auth import get_planet_key


class PlanetAssetEngine:

    def __init__(self):
        self.auth = Auth.from_key(get_planet_key())

    async def list_assets(self, item_id):

        async with Session(auth=self.auth) as sess:

            client = DataClient(sess)

            item = await client.get_item("PSScene", item_id)

            return item.get("assets", [])

    async def get_asset(self, item_id, asset_type):

        assets = await self.list_assets(item_id)

        if asset_type in assets:
            return asset_type

        return None