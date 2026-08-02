import sys

from backend.spatial.data_manager import GeoDataManager
from backend.spatial.spatial_engine import SpatialEngine


def main():

    if len(sys.argv) != 3:
        print("Usage:")
        print("python -m backend.spatial.query_location <longitude> <latitude>")
        return

    longitude = float(sys.argv[1])
    latitude = float(sys.argv[2])

    manager = GeoDataManager()

    manager.load_layer(
        "counties",
        "data/boundaries/Kenya_county.shp"
    )

    manager.load_layer(
        "roads",
        "data/roads/ken_roads.shp"
    )

    engine = SpatialEngine(manager)

    county = engine.locate_point(longitude, latitude)
    road = engine.nearest_road(longitude, latitude)

    if county.empty:
        print("Location not found.")
    else:
        print(f"County: {county['COUNTY'].iloc[0]}")
        print(f"Nearest Road: {road['ROAD_NAME'] if 'ROAD_NAME' in road else 'Unknown'}")


if __name__ == "__main__":
    main()