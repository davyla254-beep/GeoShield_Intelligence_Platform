
import folium

def create_map():

    kenya = folium.Map(
        location=[0.3, 37.8],
        zoom_start=6,
        tiles="CartoDB positron",
        control_scale=True
    )

    folium.LayerControl().add_to(kenya)

    return kenya
