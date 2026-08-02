
from models import drought

class GeoShield:

    def __init__(self, data_path):
        self.df = drought.load_drought_data(data_path)

    def highest_risk(self):
        return drought.highest_risk(self.df)

    def top10(self):
        return drought.top_risk_counties(self.df)
