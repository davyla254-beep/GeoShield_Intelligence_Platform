import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USGS_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/"
    "summary/all_day.geojson"
)

def get_earthquakes():
    try:
        response = requests.get(
            USGS_URL,
            timeout=10,
            verify=False,
            headers={
                "User-Agent": "GeoShield-AI/1.0"
            }
        )

        data = response.json()

        earthquakes = []

        for feature in data["features"]:

            prop = feature["properties"]
            geo = feature["geometry"]

            earthquakes.append({
                "place": prop["place"],
                "magnitude": prop["mag"],
                "time": prop["time"],
                "coordinates": geo["coordinates"]
            })

        return earthquakes

    except Exception as e:
        return {"error": str(e)}