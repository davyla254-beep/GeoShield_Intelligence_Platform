
import os

class GeoShieldBuilder:

    def __init__(self, project):

        self.project = project

    def create_module(self, parent, name):

        folder = os.path.join(
            self.project,
            parent,
            name.lower()
        )

        os.makedirs(folder, exist_ok=True)

        with open(
            os.path.join(folder,"__init__.py"),
            "w"
        ) as f:
            pass

        print(f"{name} module created")

