from geopy.distance import geodesic


def get_nearest_resources(disaster_location, resources, limit=5):
    """
    disaster_location = (lat, lon)

    resources = list of sqlite rows
    """

    ranked = []

    for resource in resources:

        resource_location = (
            resource["latitude"],
            resource["longitude"]
        )

        distance = geodesic(
            disaster_location,
            resource_location
        ).km

        ranked.append({

            **dict(resource),

            "distance_km": round(distance, 2)

        })

    ranked.sort(
        key=lambda x: x["distance_km"]
    )

    return ranked[:limit]