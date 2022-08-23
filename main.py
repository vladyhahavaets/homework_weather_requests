from pprint import pprint

import requests
from app_id import appid

town = 'Kyiv'
r = requests.get(f'https://api.openweathermap.org/data/2.5/find?q={town}&type=like&APPID={appid}')
content = r.json()
town_id = content['list'][0]['id']
weather_id = content['list'][0]['weather'][0]['id']

print(f'Kyiv id = {town_id}')
