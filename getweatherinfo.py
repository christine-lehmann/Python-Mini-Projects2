# Create an account to get api key -> https://home.openweathermap.org/api_keys

from urllib import request


import requests
from pprint import pprint

API_Key = 'ad2e4a30dbda7091fcd33c21589606df' # default key

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)