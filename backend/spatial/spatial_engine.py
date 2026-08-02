from shapely.geometry import Point
import geopandas as gpd


class SpatialEngine:

    def __init__(self, data_manager):
        self.data_manager = data_manager

    def get_layer(self, name):
        return self.data_manager.get_layer(name)

    def find_county(self, county_name):
        counties = self.get_layer("counties")
        return counties[counties["COUNTY"] == county_name]

    def locate_point(self, longitude, latitude):
        counties = self.get_layer("counties")

        point = Point(longitude, latitude)

        result = counties[counties.contains(point)]

        return result

    def nearest_road(self, longitude, latitude):

        roads = self.get_layer("roads")

        # Reproject roads to Kenya UTM Zone 37S
        roads_projected = roads.to_crs(epsg=32737)

        # Create the query point
        point = gpd.GeoSeries(
            [Point(longitude, latitude)],
            crs="EPSG:4326"
        ).to_crs(epsg=32737)

        # Compute distances in meters
        distances = roads_projected.distance(point.iloc[0])

        # Return the nearest road from the original layer
        nearest = roads.iloc[distances.idxmin()]

        return nearest