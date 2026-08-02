
class OSMEngine:

    def __init__(self):

        self.categories={}

    def register(self,name):

        self.categories[name]=[]

    def available(self):

        return list(self.categories.keys())

