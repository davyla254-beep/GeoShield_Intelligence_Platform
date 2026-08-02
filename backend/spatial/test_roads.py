from backend.spatial.data_manager import GeoDataManager

manager = GeoDataManager()

manager.load_layer(
    "roads",
    "data/roads/ken_roads.shp"
)

roads = manager.get_layer("roads")

if roads is None:
    print("Road layer not loaded.")
else:
    print("Columns:")
    print(roads.columns)

    print("\nFirst five roads:")
    print(roads.head())