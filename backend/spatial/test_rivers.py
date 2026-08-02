from backend.spatial.data_manager import GeoDataManager

manager = GeoDataManager()

manager.load_layer(
    "rivers",
    "data/rivers/kenya_rivers.shp"
)

rivers = manager.get_layer("rivers")

if rivers is None:
    print("River layer not loaded.")
else:
    print("Columns:")
    print(rivers.columns)

    print("\nFirst five rivers:")
    print(rivers.head())