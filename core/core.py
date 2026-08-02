
import pandas as pd
import os

class GeoShieldCore:

    def __init__(self,data_folder):

        self.data_folder=data_folder

    def load_master(self):

        path=os.path.join(
            self.data_folder,
            "county_master_intelligence.csv"
        )

        return pd.read_csv(path)
