import asyncio

from backend.satellite.satellite_manager import SatelliteManager


async def main():

    manager = SatelliteManager()

    planet = manager.provider("planet")

    scenes = await planet.latest_images(limit=3)

    print(scenes)


asyncio.run(main())