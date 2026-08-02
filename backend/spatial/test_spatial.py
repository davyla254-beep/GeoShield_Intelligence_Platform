from backend.spatial.data_manager import GeoDataManager
from backend.spatial.spatial_engine import SpatialEngine

data_manager = GeoDataManager()
data_manager.load_layer(
    "counties",
    "data/boundaries/Kenya_county.shp"
)

engine = SpatialEngine(data_manager)

print(engine.get_layer("counties").head())