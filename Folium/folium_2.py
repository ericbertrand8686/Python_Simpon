import folium
import geopandas
import json

 
iw_map = folium.Map(location=[48.7, 2.3], zoom_start=9)
gdf = geopandas.read_file('departements.geojson')

folium.GeoJson(gdf).add_to(iw_map)
folium.LayerControl().add_to(iw_map)
#folium.GeoJson('departements').add_to(iw_map)

iw_map.save('iw_map.html')

