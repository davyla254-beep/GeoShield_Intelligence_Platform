from backend.satellite.planet_search import PlanetSearchEngine
from backend.satellite.planet_assets import PlanetAssetEngine


class PlanetService:

    def __init__(self):
        self.search_engine = PlanetSearchEngine()
        self.asset_engine = PlanetAssetEngine()

    async def latest_images(
        self,
        geometry=None,
        start_date=None,
        end_date=None,
        cloud_cover=0.2,
        limit=10
    ):
        return await self.search_engine.latest_images(
            geometry=geometry,
            start_date=start_date,
            end_date=end_date,
            cloud_cover=cloud_cover,
            limit=limit
        )

    async def scene_assets(self, item_id):
        return await self.asset_engine.list_assets(item_id)

    async def latest_scene_assets(
        self,
        geometry=None,
        cloud_cover=0.2
    ):
        scenes = await self.latest_images(
            geometry=geometry,
            cloud_cover=cloud_cover,
            limit=1
        )

        if not scenes:
            return None

        scene = scenes[0]

        assets = await self.scene_assets(scene["id"])

        return {
            "scene": scene,
            "assets": assets
        }