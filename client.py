# Authors: Meyer Montagner, Pablo Villalba
# Programa que funciona como cliente al servidor. Usado como práctica del concepto de API.

import requests


""" Acceso a endpoint /1a/. 
Recibe un número como parámetro.
Retorna un JSON con el cuadrado del número. """
result1 = requests.get('http://127.0.0.1:5000/1a/?url=https://en.wikipedia.org/wiki/Interdisciplinarity')  # type: requests.Response
print(result1.text)

""" Acceso a endpoint /3a/. 
Recibe un número como parámetro.
Retorna un JSON con el cuadrado del número. """
result1 = requests.get("http://127.0.0.1:5000/3a/?value=[[%27HOLA%27],[%27BOBO%27]]")  # type: requests.Response
print(result1.text)

