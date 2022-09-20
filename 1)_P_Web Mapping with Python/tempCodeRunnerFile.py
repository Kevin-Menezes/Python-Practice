
# # Reading data from csv
# data = pandas.read_csv("1)_Web Mapping with Python/Volcanoes.txt")

# lat = list(data["LAT"])
# lon = list(data["LON"])
# elev = list(data["ELEV"])

# map = folium.Map(location=[48,-121],zoom_start=6,titles="Stamen Terrain") 


# # We use feature group to properly organise the map data
# fg = folium.FeatureGroup(name="Volcanoes map")


# # To add a location marker on the map at a particular place and taking coordinates from a csv file
# for lt, ln, el in zip(lat,lon,elev): 

#     fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+"m",icon=folium.Icon(color = 'red'))) 

# map.add_child(fg)
# map.save("Map1.html")