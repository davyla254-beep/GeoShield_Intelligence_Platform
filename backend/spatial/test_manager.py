from backend.spatial.data_manager import GeoDataManager

manager = GeoDataManager()

manager.load_layer(
    "counties",
    "data/boundaries/Kenya_county.shp"
)

print(manager.list_layers())