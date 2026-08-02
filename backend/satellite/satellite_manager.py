from backend.satellite.providers.planet_provider import PlanetProvider


class SatelliteManager:

    def __init__(self):

        self.providers = {
            "planet": PlanetProvider()
        }

    def provider(self, name):

        return self.providers[name]