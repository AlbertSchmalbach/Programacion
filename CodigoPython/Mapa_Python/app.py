import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

location_name = input("Enter a location: ")

geolacator = Nominatim(user_agent="geoapi")
location = geolacator.geocode(location_name)

if location:
    latitude = location.latitude
    longitude = location.longitude

    # Create a map centered at the location
    map = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker for the location
    folium.Marker([latitude, longitude], popup=location_name).add_to(map)

    # Save the map to an HTML file
    map.save("map.html")

    # Display the map in the notebook
    display(map)
else:
    print("Location not found. Please try again.")  
    
# Note: Make sure to install the required libraries using pip if you haven't already.
# pip install folium geopy  