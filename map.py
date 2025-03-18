import folium

def display_location(location_name, latitude, longitude):
    # Create a map centered around the specified location
    map_center = [latitude, longitude]
    my_map = folium.Map(location=map_center, zoom_start=15)

    # Add a marker for the specified location
    folium.Marker(
        location=map_center,
        popup=location_name,
        icon=folium.Icon(color='blue')
    ).add_to(my_map)

    # Save the map as an HTML file
    my_map.save('map_display.html')

if __name__ == "__main__":
    # Specify the location details
    location_name = "Your Location Name"
    latitude = 17.385044  # Replace with the actual latitude
    longitude = 78.486671  # Replace with the actual longitude

    # Display the location on the map
    display_location(location_name, latitude, longitude)
