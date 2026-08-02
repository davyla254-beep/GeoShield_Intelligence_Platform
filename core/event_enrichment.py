from backend.spatial.spatial_engine import SpatialEngine


class EventEnrichmentEngine:

    def __init__(self, data_manager):

        self.spatial = SpatialEngine(data_manager)

    def enrich(self, longitude, latitude):

        county = self.spatial.locate_point(
            longitude,
            latitude
        )

        road = self.spatial.nearest_road(
            longitude,
            latitude
        )

        if county.empty:
            county_name = "Unknown"
        else:
            county_name = county["COUNTY"].iloc[0]

        return {

            "longitude": longitude,

            "latitude": latitude,

            "county": county_name,

            "road_type": road["RTT_DESCRI"],

            "road_surface": road["MED_DESCRI"]

        }