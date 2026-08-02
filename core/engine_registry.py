

class EngineRegistry:

    def __init__(self):

        self.engines={}

    def register(self,engine):

        self.engines[engine.name]=engine

    def list(self):

        return list(self.engines.keys())

