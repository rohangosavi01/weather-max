'''  
Structure of custom dictionary ->     
    city      = City Name
    coord     = List of Coordinated [long, lat ]
    weather   = List of weather data [icon, description]
    stats     = List of stats [Tempreture, feels, max, min, pressure, humidity]
    wind      = wind Speed
    visi      = Visibility 
'''


def customDataDictionary(dictionary):
    if dictionary == 'city-not-found':
        return 'city-not-found'
    
    rain = '"Rain is grace; rain is the sky descending to the earth; without rain, there would be no life."'
    thunderstrom = '“Thunderstorms are as much our friends as the sunshine.”'
    drizzle = 'Drizzle happiness wherever you go.'
    clouds = '“There are no rules of architecture for a castle in the clouds.”'
    clear = '"The sky is the limit. You never have the same experience twice."'
    snow = '“A snowball in the face is surely the perfect beginning to a lasting friendship.”'
    general = 'Wherever you go, no matter what the weather, always bring your own sunshine.'

    city = dictionary['name']
    coord = [dictionary['coord']['lon'], dictionary['coord']['lat']]
    weather = [dictionary['weather'][0]['main'], dictionary['weather']
               [0]['description'], dictionary['weather'][0]['icon']]
    
    stats = [round(dictionary['main']['temp'], 2), round(dictionary['main']['feels_like'], 2), round(dictionary['main']['temp_max'], 2), round(dictionary['main']['temp_min'], 2)]
    wind = dictionary['wind']['speed']
    visibility = dictionary['visibility']

    if int(dictionary['weather'][0]['id']) >= 200 and int(dictionary['weather'][0]['id']) <= 299:
        selection = thunderstrom
    
    elif int(dictionary['weather'][0]['id']) >= 300 and int(dictionary['weather'][0]['id']) <=399:
        selection = drizzle
    
    elif int(dictionary['weather'][0]['id']) >= 500 and int(dictionary['weather'][0]['id']) <= 599:
        selection = rain

    elif int(dictionary['weather'][0]['id']) >= 600 and int(dictionary['weather'][0]['id']) <= 699:
        selection = snow
    
    elif int(dictionary['weather'][0]['id']) >= 700 and int(dictionary['weather'][0]['id']) <= 799:
        selection = general
    
    elif int(dictionary['weather'][0]['id']) == 800: 
        selection = clear
    
    elif int(dictionary['weather'][0]['id']) >= 801 and int(dictionary['weather'][0]['id']) <= 809:
        selection = clouds
    
    customDictionary = {'city':city, 'coord':coord, 'weather':weather, 'stats':stats,'wind':wind, 'visibility':visibility, 'selection':selection}
    
    return customDictionary








