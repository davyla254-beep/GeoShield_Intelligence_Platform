from pathlib import Path

import geopandas as gpd


class GeoDataManager:
    def __init__(self):
        self.layers = {}

    def load_layer(self, name, filepath):
        path = Path(filepath)

        if not path.exists():
            raise FileNotFoundError(f"{filepath} not found.")

        self.layers[name] = gpd.read_file(path)

        print(f"{name} loaded successfully.")

    def get_layer(self, name):
        return self.layers.get(name)

    def list_layers(self):
        return list(self.layers.keys())