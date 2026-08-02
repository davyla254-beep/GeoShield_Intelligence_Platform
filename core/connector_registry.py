
class ConnectorRegistry:

    def __init__(self):

        self.connectors = {}

    def register(self, name, connector):

        self.connectors[name] = connector

    def get(self, name):

        return self.connectors.get(name)

    def list(self):

        return list(self.connectors.keys())
