from planet import Session
from planet.clients import DataClient
from planet import Auth

from backend.satellite.auth import get_planet_key


class PlanetDownloadEngine:

    def __init__(self):
        self.auth = Auth.from_key(get_planet_key())

    async def activate_download(
        self,
        scene_id,
        asset_type="ortho_visual"
    ):

        async with Session(auth=self.auth) as sess:

            client = DataClient(sess)

            # Get all assets for the scene
            print("Downloading scene:", scene_id)
            assets = await client.list_item_assets(
                "PSScene",
                scene_id
            )

            # Check whether the requested asset exists
            if asset_type not in assets:
                raise ValueError(
                    f"{asset_type} not available.\n"
                    f"Available assets:\n{list(assets.keys())}"
                )

            asset = assets[asset_type]

            print("\nSELECTED ASSET\n")
            print(asset)

            return asset