GIT-WEATHERED 

    Tu prónostico a Comandos

Desarrollo de una aplicación CLI que consulte una API de clima y muestre la información climática en la terminal

Resumen:

    Esta versión inicial permite consultar el clima actual de cualquier ciudad utilizando datos de OPEN-METEO. La aplicación devuelve información como temperatura, humedad, viento. Se puede obtener la salida en formato TEXTO, JSON y CSV .

Características:

    Consulta del clima en tiempo real.
    Formatos de salida: JSON, TEXTO y CSVE.
    Datos proporcionados:
    Ciudad -Pais.
    Temperatura, humedad, viento.

Uso:

    Clima en formato texto (predeterminado): python3 cli.py formatotexto Asuncion
    Clima en formato JSON: python3 cli.py formatojson Asuncion
	Clima en formato CSV: python3 cli.py formatocsv Asuncion

Requisitos:

    Librerías: requests, typer.

