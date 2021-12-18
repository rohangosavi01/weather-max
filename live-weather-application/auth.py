import requests, json

def request_weather(city):
    token = '18adfd08d3ac94dfa82cff135fef7927'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+token
    response = requests.get(base_url)
    data = response.json()
    
    if data['cod'] == '404' or data['cod'] == 404:
        return 'city-not-found'

    return data


