import requests

# Make API requests and process the response data
# OpenWeatherMap API
weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=40.659205&lon=-73.890690&appid=2107eb86cf98a0f11bc1e189774d9cd2'
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

# Google Maps API
map_url = 'https://us1.locationiq.com/v1/search.php?key=pk.8622b5424a77e497308bc53f91e0e741&q=New%20York&format=json'
map_response = requests.get(map_url)
map_data = map_response.json()

# Wikivoyage API (free access)
wikivoyage_url = 'https://en.wikivoyage.org/w/api.php?action=query&format=json&prop=extracts&titles=Paris'
wikivoyage_response = requests.get(wikivoyage_url)
wikivoyage_data = wikivoyage_response.json()

weather_description = weather_data["weather"][0]["description"]
location_lat = wikivoyage_data[0]['lat']
location_long = wikivoyage_data[0]['lon']

print(weather_description)
print(location_lat)
print(location_long)
