# coding: utf-8
import requests

params = {
    'access_key': 'b5712576b97e3d74db8d01d5385e465f',
    'query': 'Irkutsk'
}

def get_current_weather():
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return api_response



#print(api_response)
city = get_current_weather()['location']['name']
temperature_c  = get_current_weather()['current']['temperature']

print(f'Current temperature in {city} is {temperature_c} C'  )