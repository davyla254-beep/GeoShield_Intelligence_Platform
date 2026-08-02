import requests

# PASTE YOUR MAP KEY HERE
MAP_KEY = "679a92b9521d5d4968bfe2ac818d265f"

# Kenya bounding box:
# West, South, East, North
KENYA_BBOX = "33.5,-5.2,42.3,5.5"

URL = (
    f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/"
    f"{MAP_KEY}/VIIRS_SNPP_NRT/"
    f"{KENYA_BBOX}/1"
)


def get_wildfires():
    try:
        response = requests.get(URL, timeout=20)
        response.raise_for_status()

        lines = response.text.splitlines()

        if len(lines) <= 1:
            return []

        headers = lines[0].split(",")

        fires = []

        for row in lines[1:]:
            values = row.split(",")

            item = dict(zip(headers, values))

            fires.append({
                "latitude": float(item["latitude"]),
                "longitude": float(item["longitude"]),
                "brightness": float(item.get("bright_ti4", 0)),
                "confidence": item.get("confidence", ""),
            })

        return fires

    except Exception as e:
        return {"error": str(e)}