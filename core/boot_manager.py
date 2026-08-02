
class BootManager:

    def __init__(self):

        self.steps=[]

    def add(self,step):

        self.steps.append(step)

    def boot(self):

        print("===== GeoShield Boot =====")

        for step in self.steps:

            print("✓",step)

        print("==========================")
