from abc import ABC, abstractmethod
from typing import Any


class SatelliteProvider(ABC):

    @abstractmethod
    async def latest_images(self, **kwargs) -> Any:
        pass

    @abstractmethod
    async def scene_assets(self, scene_id: str) -> Any:
        pass

    @abstractmethod
    async def download_scene(
        self,
        scene_id: str,
        asset_type: str
    ) -> Any:
        pass