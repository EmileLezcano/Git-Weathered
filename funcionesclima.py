import requests

def get_location(city):

    url_location = (f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=es&format=json")
    location_response = requests.get(url_location)
    
    if location_response.status_code == 200:

        location_data = location_response.json()

        if 'results' in location_data and len(location_data['results']) > 0:

            return location_data['results'][0]['latitude'], location_data['results'][0]['longitude']
        else:

            print("No se encontraron resultados para la ciudad ingresada")
            
            return None, None
    else:
        
        print("Error al momento de obtener los datos de la ubicación")
        
        return None, None        

def get_weather_data(lati,longi):
    url_weather = (f"https://api.open-meteo.com/v1/forecast?latitude={lati}&longitude={longi}&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m")
    weather_response = requests.get(url_weather)

    if weather_response.status_code == 200:

        return weather_response.json()
    
    else:
        
        print("Error al momento de obtener los datos del clima")
        
        return None
    
