from pprint import pprint

import requests
from app_id import appid

town = 'Kyiv'
r = requests.get(f'https://api.openweathermap.org/data/2.5/find?q={town}&type=like&APPID={appid}')
content = r.json()
# pprint(content)

town_id = content['list'][0]['id']
weather_id = content['list'][0]['weather'][0]['id']

print(f'Kyiv id = {town_id}')

res = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                   params={'id': town_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

data = res.json()
# pprint(data)

data_town = data['city']['name']
temperature = data['list'][0]['main']['temp']
humidity = data['list'][0]['main']['humidity']
wind_speed = data['list'][3]['wind']['speed']

print(f"У місті {data_town} температура сягає {temperature} градусів за Цельсієм, вологість складає {humidity} %,"
      f"швидкість вітру дорівнює {wind_speed} метрів на секунду ")
