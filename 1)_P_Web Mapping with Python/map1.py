import folium
import pandas

# lat = -90 to 90 | lon = -180 to 180

# #To create a map
# map = folium.Map(location=[50,10],zoom_start=6,titles="Stamen Terrain") 
# map.save("Map1.html")

# # We use feature group to properly organise the map data and then collectively add the feature group as a child of the map
# fg = folium.FeatureGroup(name="My Map")

# # To add a location marker on the map at a particular place
# for coordinates in [[51.1657,10.4515],[52,10]]: # list of coordinates...every iteration considers 1 pair of lat+lon

#     fg.add_child(folium.Marker(location=coordinates, popup="This is a Marker",icon=folium.Icon(color = 'red'))) 

# map.add_child(fg)
# map.save("Map1.html")

# ----------------------------------------------- Normal method -----------------------------------------------------------------

# Reading data from csv
data = pandas.read_csv("1)_Web Mapping with Python/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[48,-121],zoom_start=6,titles="Stamen Terrain") 


# We use feature group to store data in a single grp and then collectively add them to the map
fg = folium.FeatureGroup(name="Volcanoes map")


# To add a location marker on the map at a particular place and taking coordinates from a csv file
for lt, ln, el in zip(lat,lon,elev): # 1st iteration we go to the 1st element of each of the 3 list

    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+"m",icon=folium.Icon(color = 'red'))) 

map.add_child(fg)
map.save("1)_Web Mapping with Python/Map1.html")


# ----------------------------------------------- Printing out volcano details in html -----------------------------------------------------------------

data = pandas.read_csv("1)_Web Mapping with Python/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
 
html = """<h4>Volcano information:</h4>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
 
map.add_child(fg)
map.save("1)_Web Mapping with Python/Map1_popup_simple.html")

# ----------------------------------------------- Printing out link & details in html advanced -----------------------------------------------------------------

data = pandas.read_csv("1)_Web Mapping with Python/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
map.add_child(fg)
map.save("1)_Web Mapping with Python/Map1_popup_advanced.html")

# # ----------------------------------------------- Normal method with different colors according to height of mountain -----------------------------------------------------------------

# Reading data from csv
data = pandas.read_csv("1)_Web Mapping with Python/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<= elevation <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[48,-121],zoom_start=6,titles="Stamen Terrain") 


# We use feature group to properly organise the map data
fg = folium.FeatureGroup(name="Volcanoes map")


# To add a location marker on the map at a particular place and taking coordinates from a csv file
for lt, ln, el in zip(lat,lon,elev): 

    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m",fill_color = color_producer(el), color = "black", fill_opacity=0.7)) 

map.add_child(fg)
map.save("1)_Web Mapping with Python/Map1_color_markers.html")


# ---------------------- Normal method with different colors according to height of mountain and population of the world using geo json --------------------------------------------------------------

# Reading data from csv
data = pandas.read_csv("1)_Web Mapping with Python/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<= elevation <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[48,-121],zoom_start=6,titles="Stamen Terrain") 


# We use feature group to properly organise the map data
fgv = folium.FeatureGroup(name="Volcanoes map")


# To add a location marker on the map at a particular place and taking coordinates from a csv file
for lt, ln, el in zip(lat,lon,elev): 

    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m",fill_color = color_producer(el), color = "black", fill_opacity=0.7)) 


# We use feature group to properly organise the map data
fgp = folium.FeatureGroup(name="Population map")

fgp.add_child(folium.GeoJson(data=open("1)_Web Mapping with Python/world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) # To choose which folium group will be displayed 
map.save("1)_Web Mapping with Python/Map1_population.html")