import asyncio

from backend.satellite.planet_assets import PlanetAssetEngine

SCENE_ID = "20260726_170618_52_24d8"

async def main():

    engine = PlanetAssetEngine()

    asset = await engine.get_asset(
        SCENE_ID,
        "ortho_visual"
    )

    print(asset)

asyncio.run(main())