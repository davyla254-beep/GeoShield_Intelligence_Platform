from dotenv import load_dotenv
import os

load_dotenv()

PLANET_API_KEY = os.getenv("PLANET_API_KEY")


def get_planet_key():
    if not PLANET_API_KEY:
        raise ValueError("Planet API Key not found.")
    return PLANET_API_KEY