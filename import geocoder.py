import geocoder
import json

# Create a list of countries
countries = ["United States", "China", "Japan", "Germany", "United Kingdom"]

# Create a GeoJSON object
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Iterate over the countries and add them to the GeoJSON object
for country in countries:

    # Get the geographic coordinates of the country
    coordinates = geocoder.google(country).latlng

    # Create a GeoJSON feature for the country
    feature = {
        "type": "Feature",
        "properties": {
            "name": country
        },
        "geometry": {
            "type": "Point",
            "coordinates": coordinates
        }
    }

    # Add the feature to the GeoJSON object
    geojson["features"].append(feature)

# Write the GeoJSON object to a file
with open("countries.geojson", "w") as f:
    json.dump(geojson, f)
