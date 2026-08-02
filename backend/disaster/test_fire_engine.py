from backend.disaster.fire_engine import FireIntelligenceEngine

engine = FireIntelligenceEngine()

fires = engine.analyse(
    "data/fires/kenya_fires.csv"
)

print(fires[:3])