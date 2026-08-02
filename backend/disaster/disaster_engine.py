class DisasterEngine:

    def __init__(self):
        self.active_disasters = []

    def add_disaster(self, disaster):

        self.active_disasters.append(disaster)

    def list_disasters(self):

        return self.active_disasters