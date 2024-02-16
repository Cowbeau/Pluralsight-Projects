import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=87037df0b7484f1e86e232241241402&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, 'is', description, 'and', temp, 'degrees.')

