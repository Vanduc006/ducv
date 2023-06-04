import geocoder
import folium
import win10toast

get_ip = input('ip here :')
ip_in4 = geocoder.ip(get_ip)
my_add = ip_in4.latlng

print(my_add)

my_map = folium.Map(location=my_add, zoom_start=14)

folium.Marker(my_add, popup='<i> TARGET </i>', tooltip= ' click here').add_to(my_map)
my_map.save('geo.html')
