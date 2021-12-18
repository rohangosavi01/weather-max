import requests
def request_weather(city):
    token = '29fe6ea557df3e8d8182eafbfa668f8c'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+token
    response = requests.get(base_url)
    data = response.json()
     
    if data['cod'] == '404' or data['cod'] == 404:
        return 'city-not-found'

    return data
