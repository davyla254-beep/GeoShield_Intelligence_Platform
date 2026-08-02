import time


class SatelliteScheduler:

    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

        while self.running:

            print("Updating satellite data...")

            # Later we will call every engine here

            time.sleep(300)

    def stop(self):
        self.running = False