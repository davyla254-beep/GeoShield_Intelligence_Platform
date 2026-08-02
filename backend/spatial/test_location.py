from backend.spatial.data_manager import GeoDataManager
from backend.spatial.spatial_engine import SpatialEngine

manager = GeoDataManager()

manager.load_layer(
    "counties",
    "data/boundaries/Kenya_county.shp"
)

engine = SpatialEngine(manager)

location = engine.locate_point(36.8219, -1.2921)

print(location["COUNTY"].iloc[0])