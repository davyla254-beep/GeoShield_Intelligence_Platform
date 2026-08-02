import asyncio

from planet import Auth
from backend.satellite.auth import get_planet_key


async def main():
    key = get_planet_key()

    auth = Auth.from_key(key)

    print("Planet SDK authentication successful.")
    print(auth)


asyncio.run(main())