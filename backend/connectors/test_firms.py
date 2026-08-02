from backend.connectors.firms_connector import FIRMSConnector

print("=== NEW TEST_FIRMS IS RUNNING ===")

connector = FIRMSConnector()

connector.load_csv(
    "data/fires/kenya_fires.csv"
)

fires = connector.get_disasters()

print(f"Total fires: {len(fires)}")
print(fires[:3])