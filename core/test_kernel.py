from core.kernel import GeoShieldKernel

kernel = GeoShieldKernel()

results = kernel.run_fire_pipeline(
    "data/fires/kenya_fires.csv"
)

print(results[:3])