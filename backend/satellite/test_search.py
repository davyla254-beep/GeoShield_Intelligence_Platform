import asyncio

from backend.satellite.planet_search import PlanetSearchEngine


async def main():

    engine = PlanetSearchEngine()

    results = await engine.latest_images(
        cloud_cover=0.1,
        limit=5
    )

    print("\nLatest Planet Images\n")

    for image in results:
        print(image)


asyncio.run(main())