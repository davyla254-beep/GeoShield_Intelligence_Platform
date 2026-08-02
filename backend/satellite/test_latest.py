import asyncio

from backend.satellite.planet_search import PlanetSearchEngine


async def main():

    engine = PlanetSearchEngine()

    images = await engine.latest_images(limit=5)

    print("\nLATEST IMAGES\n")

    for img in images:

        print("-" * 30)
        print("ID:", img["id"])
        print("Published:", img["published"])
        print("Stage:", img["stage"])
        print("Quality:", img["quality"])
        print("Cloud:", img["cloud"])


asyncio.run(main())