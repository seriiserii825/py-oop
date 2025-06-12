import folium


def my_folium():
    inty = 5
    listy = [6, 7]
    stringy = "Hi"

    azores = folium.folium.Map(location=(38, -27), zoom_start=6)
    azores.save("azores.html")
