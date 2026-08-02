import asyncio
from datetime import datetime

from backend.services.fire_monitor import check_kenya_fire


system_state = {
    "fire": False,
    "flood": False,
    "earthquake": False,
    "disease": False,
    "cyber": False,
    "last_update": None,
    "alerts": []
}


async def ai_loop():

    while True:

        system_state["last_update"] = str(datetime.now())

        system_state["alerts"] = []

        await check_fire()

        await check_flood()

        await check_earthquake()

        await check_disease()

        await check_cyber()

        await asyncio.sleep(30)


async def check_fire():

    result = check_kenya_fire()

    if result["status"] == "active":

        system_state["fire"] = True

        for hotspot in result["hotspots"]:

            system_state["alerts"].append({

                "type": "fire",

                "latitude": hotspot["latitude"],

                "longitude": hotspot["longitude"],

                "brightness": hotspot["brightness"],

                "frp": hotspot["frp"],

                "message": "Live wildfire detected",

                "time": hotspot["date"] + " " + hotspot["time"]

            })

    else:

        system_state["fire"] = False


async def check_flood():
    pass


async def check_earthquake():
    pass


async def check_disease():
    pass


async def check_cyber():
    pass