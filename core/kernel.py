from backend.disaster.fire_engine import FireIntelligenceEngine


class GeoShieldKernel:

    def __init__(self):

        self.fire_engine = FireIntelligenceEngine()

    def run_fire_pipeline(self, filepath):

        print("===================================")
        print(" GEO SHIELD KERNEL STARTED")
        print("===================================")

        fires = self.fire_engine.analyse(filepath)

        print(f"Processed {len(fires)} fire events.")

        return fires