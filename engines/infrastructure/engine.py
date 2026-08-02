
class InfrastructureEngine:

    def __init__(self):

        self.layers={}

    def register(self,name,data):

        self.layers[name]=data

    def available_layers(self):

        return list(self.layers.keys())

