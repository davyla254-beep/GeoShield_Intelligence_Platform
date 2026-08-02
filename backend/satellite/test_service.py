import asyncio

from backend.satellite.planet_service import PlanetService


async def main():

    service = PlanetService()

    result = await service.latest_scene_assets()

    if result is None:
        print("No scenes found.")
        return

    print("\nLATEST SCENE\n")
    print(result["scene"])

    print("\nASSETS\n")
    print(result["assets"])


asyncio.run(main())