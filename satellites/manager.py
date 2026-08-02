
class SatelliteManager:

    def __init__(self):

        self.sources={}

    def register(self,name,source):

        self.sources[name]=source

    def available(self):

        return list(self.sources.keys())

