from backend.spatial.data_manager import GeoDataManager
from backend.spatial.spatial_engine import SpatialEngine


class SpatialQueryEngine:

    def __init__(self):

        self.data_manager = GeoDataManager()

        self.data_manager.load_layer(
            "counties",
            "data/boundaries/Kenya_county.shp"
        )

        self.data_manager.load_layer(
            "roads",
            "data/roads/ken_roads.shp"
        )

        self.engine = SpatialEngine(self.data_manager)

    def query_location(self, longitude, latitude):

        county = self.engine.locate_point(longitude, latitude)
        road = self.engine.nearest_road(longitude, latitude)

        return {
            "longitude": longitude,
            "latitude": latitude,
            "county": county["COUNTY"].iloc[0],
            "nearest_road": road["ROAD_NAME"] if "ROAD_NAME" in road else "Unknown"
        }