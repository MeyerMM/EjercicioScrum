# Developers: Meyer Montagner, Pablo Villalba
# Scrum Manager: Damaso
# Programa que funciona como cliente al servidor. Usado como práctica de Scrum.

import requests


""" Acceso a endpoint /1a/. 
Recibe desde la ruta una direccion web
    Retorna  el texto de la direccion"""
result1 = requests.get("http://127.0.0.1:5001/1a/?url=https://en.wikipedia.org/wiki/Interdisciplinarity")  # type: requests.Response
print(result1.text)


""" Acceso a endpoint /2a/. 
Recibe un texto como parámetro.
Retorna un JSON con el texto separado en una lista de listas. """
result2 = requests.get("http://127.0.0.1:5001/2a/?texto= Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quis consectetur justo. Maecenas porta aliquet arcu sed iaculis. Maecenas tincidunt venenatis quam, in posuere libero tempus at. Curabitur porttitor sed lorem a luctus. Nam ut nisl eu odio pretium aliquet at in ante. Fusce euismod venenatis dictum. Ut pulvinar bibendum justo sit amet accumsan. Suspendisse quis orci eget magna eleifend auctor. Sed ultrices turpis sit amet odio aliquet sodales. In hac habitasse platea dictumst. Maecenas sed arcu vel arcu condimentum rhoncus in eget lectus. Aliquam et libero elit. Duis nisl nisl, ullamcorper sed turpis nec, varius volutpat nunc. Pellentesque tincidunt eget magna sit amet efficitur. Mauris lacinia, libero ac imperdiet viverra, nisl magna auctor arcu, sit amet iaculis lorem velit ut nisl. Sed vitae placerat velit. Sed sit amet lorem vel erat fermentum malesuada et quis justo. In vitae laoreet justo. Mauris nisl nibh, gravida vel mi a, elementum condimentum tellus. Nulla et orci id tortor facilisis pharetra. Fusce ac metus in mi iaculis congue consequat quis est. Suspendisse accumsan vehicula elementum. Maecenas dictum tempor eros. Proin ut mauris malesuada, laoreet lorem sit amet, porta metus.")  # type: requests.Response
print(result2.text)


""" Acceso a endpoint /3a/. 
Recibe desde la ruta una lista de listas con texto
    Retorna una lista de listas con todo el texto en minuscula"""
result3 = requests.get("http://127.0.0.1:5001/3a/?value=[[%27HOLA%27],[%27BOBO%27]]")  # type: requests.Response
print(result3.text)


""" Acceso a endpoint /4a/. 
Recibe una lista de listas con strings como parámetro.
Retorna un JSON con los strings ordenados alfabeticamente en una lista de listas. """
result4 = requests.get("http://127.0.0.1:5001/4a/?value=[['e', 'i', 'u', 'a', 'o'],['z', 'g', 't', 'b', 'm']]")  # type: requests.Response
print(result4.text)
