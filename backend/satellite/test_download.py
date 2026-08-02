import asyncio

from backend.satellite.planet_download import PlanetDownloadEngine


SCENE_ID = "20200617_204449_0f17"


async def main():

    engine = PlanetDownloadEngine()

    await engine.activate_download(SCENE_ID)


asyncio.run(main())