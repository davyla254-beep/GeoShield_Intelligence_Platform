import csv
from pathlib import Path


class FIRMSConnector:

    def __init__(self):

        self.disasters = []

        self.project_root = Path(__file__).resolve().parents[2]

    def load_csv(self, filepath):

        path = self.project_root / filepath

        if not path.exists():
            raise FileNotFoundError(f"{path} not found.")

        self.disasters = []

        with open(path, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                disaster = {

                    "id": f'{row["latitude"]}_{row["longitude"]}',

                    "type": "Fire",

                    "latitude": float(row["latitude"]),

                    "longitude": float(row["longitude"]),

                    "brightness": float(row["bright_ti4"]),

                    "frp": float(row["frp"]),

                    "confidence": row["confidence"],

                    "satellite": row["satellite"],

                    "instrument": row["instrument"],

                    "date": row["acq_date"],

                    "time": row["acq_time"],

                    "daynight": row["daynight"]

                }

                self.disasters.append(disaster)

        print(f"{len(self.disasters)} fire records loaded successfully.")

    def get_disasters(self):

        return self.disasters