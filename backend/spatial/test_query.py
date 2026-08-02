from backend.spatial.query_engine import SpatialQueryEngine

query = SpatialQueryEngine()

result = query.query_location(
    36.8219,
    -1.2921
)

print(result)