from backend.satellite.providers.base import SatelliteProvider
from backend.satellite.planet_service import PlanetService


class PlanetProvider(SatelliteProvider):

    def __init__(self):
        self.service = PlanetService()

    async def latest_images(self, **kwargs):
        return await self.service.latest_images(**kwargs)

    async def scene_assets(self, scene_id):
        return await self.service.scene_assets(scene_id)

    async def download_scene(self, scene_id, asset_type):
        return {
            "message": "Planet download requires asset entitlement."
        }