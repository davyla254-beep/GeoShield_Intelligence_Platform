

class GeoShieldManager:

    def __init__(self):

        self.engines={}

        self.connectors={}

    def register_engine(self,engine):

        self.engines[engine.name]=engine

