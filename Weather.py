import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=40.659205&lon=-73.890690&appid=0023c10b6c1582cb4741a42787b3a2cd"
CITY = "New York"

def Kelvin_to_celsius_fahrenheit (kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 35
    return celsius, fahrenheit

url = BASE_URL + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheight = Kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = Kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheight}°F")
print(f"Temperature in {CITY}: feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"sun rise in {CITY} at {description}")
print(f"sun rise in {CITY} at {sunrise_time} local time")
print(f"sun set in {CITY} at {sunset_time} local time")
print(f"General weather in  {CITY}: {description}")