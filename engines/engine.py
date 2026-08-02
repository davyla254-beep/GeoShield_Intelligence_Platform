

class Engine:

    def __init__(self,name):

        self.name=name

        self.status="offline"

    def start(self):

        self.status="online"

    def stop(self):

        self.status="offline"

