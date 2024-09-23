import json
import csv
import io
import typer  # Se importa la biblioteca typer para trabajar con CLI

# Importar las funciones desde apicli.py
from funcionesclima import get_location, get_weather_data

app = typer.Typer()

@app.command()
def formatotexto(city: str):
    """Muestra los datos en texto normal"""
    # Obtener la latitud y longitud de la ciudad
    latitude, longitude = get_location(city)

    # Si se obtuvieron correctamente la latitud y longitud
    if latitude and longitude:
        weather_data = get_weather_data(latitude, longitude)

        if weather_data:
            # Mostrar el pronóstico del tiempo
            print("Pronóstico del tiempo en", city)
            key = weather_data['current']
            print("Temperatura:", key['temperature_2m'], "C")
            print("Humedad:", key['relative_humidity_2m'], "%")
            print("Viento:", key['wind_speed_10m'], "km/h")

            temp = key['temperature_2m']
            hum = key['relative_humidity_2m']
            vel = key['wind_speed_10m']
            weather_data_dic = {
                'Ciudad': city,
                'Temperatura': temp,
                'Humedad': hum,
                'Viento': vel
            }

        else:
            print("No se pudo obtener el pronóstico del tiempo")
    else:
        print("No se pudo obtener la ubicación de la ciudad")


@app.command()
def formatojson(city: str):
    """Muestra los datos en formato json"""
    # Obtener la latitud y longitud de la ciudad
    latitude, longitude = get_location(city)

    # Si se obtuvieron correctamente la latitud y longitud
    if latitude and longitude:
        weather_data = get_weather_data(latitude, longitude)

        if weather_data:
            # Obtener los datos y guardar en un diccionario
            key = weather_data['current']
            temp = key['temperature_2m']
            hum = key['relative_humidity_2m']
            vel = key['wind_speed_10m']
            weather_data_dic = {
                'Ciudad': city,
                'Temperatura': temp,
                'Humedad': hum,
                'Viento': vel
            }

            # Convertir los datos a JSON y mostrarlos
            weather_data_json = json.dumps(weather_data_dic, indent=4, ensure_ascii=False)  # ensure_ascii=False se usa para manejar caracteres especiales correctamente.
            print("Pronóstico del tiempo en", city)
            print(weather_data_json)

        else:
            print("No se pudo obtener el pronóstico del tiempo")
    else:
        print("No se pudo obtener la ubicación de la ciudad")

@app.command()
def formatocsv(city: str):
    """Muestra los datos en formato csv"""
    # Obtener la latitud y longitud de la ciudad
    latitude, longitude = get_location(city)

    # Si se obtuvieron correctamente la latitud y longitud
    if latitude and longitude:
        weather_data = get_weather_data(latitude, longitude)

        if weather_data:
            # Obtener los datos y guardar en un diccionario
            key = weather_data['current']
            temp = key['temperature_2m']
            hum = key['relative_humidity_2m']
            vel = key['wind_speed_10m']
            weather_data_dic = {
                'Ciudad': city,
                'Temperatura': temp,
                'Humedad': hum,
                'Viento': vel
            }
            # Convertir los datos a CSV y mostrarlos
            output = io.StringIO()  # Se crea un objeto StringIO llamado output para almacenar los datos CSV en memoria.
            writer = csv.DictWriter(output, fieldnames=weather_data_dic.keys())  # Se usa csv.DictWriter para escribir los datos del diccionario en el objeto StringIO.
            writer.writeheader()
            writer.writerow(weather_data_dic)
            csv_data = output.getvalue()
            output.close()

            print("Pronóstico del tiempo en", city)
            print(csv_data)
        else:
            print("No se pudo obtener el pronóstico del tiempo")
    else:
        print("No se pudo obtener la ubicación de la ciudad")


if __name__ == "__main__":
    app()
