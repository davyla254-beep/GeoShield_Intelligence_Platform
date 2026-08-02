"""
GeoShield Satellite Manager

Central gateway for all satellite engines.
"""

from backend.satellite.sentinel2.sentinel import SentinelEngine
from backend.satellite.sentinel2.ndvi import NDVIEngine
from backend.satellite.sentinel2.cropstress import CropStressEngine

from backend.satellite.sentinel1.flood import FloodEngine

from backend.satellite.viirs.viirs import VIIRSEngine

from backend.satellite.gpm.gpm import GPMEngine

from backend.satellite.era5.weather import WeatherEngine

from backend.satellite.ai.drought import DroughtEngine


class SatelliteManager:

    def __init__(self):

        # Satellite Engines
        self.sentinel = SentinelEngine()
        self.viirs = VIIRSEngine()
        self.gpm = GPMEngine()
        self.weather = WeatherEngine()

        # Analysis Engines
        self.ndvi = NDVIEngine()
        self.cropstress = CropStressEngine()
        self.flood = FloodEngine()
        self.drought = DroughtEngine()

    def status(self):
        return {
            "Sentinel-2": self.sentinel.name,
            "VIIRS": self.viirs.name,
            "GPM": self.gpm.name,
            "ERA5": self.weather.name,
            "NDVI": self.ndvi.name,
            "Crop Stress": self.cropstress.name,
            "Flood": self.flood.name,
            "Drought": self.drought.name,
        }