
import geopandas as gpd

def load_counties(path):
    return gpd.read_file(path)
