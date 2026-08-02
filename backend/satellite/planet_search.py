from planet import Session
from planet.clients import DataClient
from planet import Auth

from backend.satellite.auth import get_planet_key


class PlanetSearchEngine:

    def __init__(self):
        self.auth = Auth.from_key(get_planet_key())

    async def latest_images(
        self,
        geometry=None,
        start_date=None,
        end_date=None,
        cloud_cover=0.2,
        limit=10
    ):

        filters = []

        if start_date and end_date:
            filters.append({
                "type": "DateRangeFilter",
                "field_name": "acquired",
                "config": {
                    "gte": start_date,
                    "lte": end_date
                }
            })

        filters.append({
            "type": "RangeFilter",
            "field_name": "cloud_cover",
            "config": {
                "lte": cloud_cover
            }
        })

        search_filter = {
            "type": "AndFilter",
            "config": filters
        }

        async with Session(auth=self.auth) as sess:

            client = DataClient(sess)

            results = []

            async for item in client.search(
                item_types=["PSScene"],
                search_filter=search_filter,
                geometry=geometry,
                sort="published asc",
                limit=100
            ):

                stage = item["properties"].get("publishing_stage", "")
                quality = item["properties"].get("quality_category", "")

               

                results.append({
                    "id": item["id"],
                    "published": item["properties"]["published"],
                    "stage": stage,
                    "quality": quality,
                    "cloud": item["properties"]["cloud_cover"]
                })

            return results