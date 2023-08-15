import json
import datetime as dt
import requests

Url = "https://api.openweathermap.org/data/2.5/weather?lat=40.659205&lon=-73.890690&appid=0023c10b6c1582cb4741a42787b3a2cd"
city = "Brooklyn"

responses = requests.get(Url)
data = responses.json()

print(data)

temperature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
weather_conditions = data['weather'][0]['description']

print("Weather in city: " + city)
print("Temperature: " + str(temperature) + " °C ")
print("Humidity: " + str(humidity) + " %")
print("Wind Speed " + str(wind_speed) + " mph ")