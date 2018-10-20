# Developers: Meyer Montagner, Pablo Villalba
# Scrum Manager: Dámaso González Pino
# Programa que inicia un servidor usado como práctica de Scrum.

"""
Conseguimos tener todos los puntos funcionales a tiempo para la última reunión a pesar de las dificultades que nos
llevaron a no completar todos los puntos en los diferentes hitos.

La parte 1a la realizó Meyer donde en un principio solo faltaba meterlo en json que consiguió terminar a tiempo.
El punto 2a la realizó Pablo, quien consiguió separarlo en párrafos pero sin utilizar NLTK. Consiguió que funcione de
otra manera porque daba problemas al importar la librería. Finalmente consiguió que todo funcione como pedía este apartado.
El punto 3a (pasar de string a lista que solo contenga minúsculas) lo hizo Meyer al cual se le complicó un poco y le
dimos apoyo intentando buscar la mejor solución que consiguió terminar justo a tiempo para la última reunión con el cliente.
El apartado 4a lo realizó Pablo sin demasiada dificultad, tuvo que devolver una lista con las cadenas ordenar
alfabéticamente. Lo que yo (Dámaso) hice es ir buscando las posibles soluciones de los puntos 3a y 4a, ayudarlos en los
puntos en los que se atascaron y la comunicación con el cliente.
"""


from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import urllib.request
import ast
import nltk


app = Flask(__name__)                           # type: Flask


@app.route('/1a/', methods=['GET'])
def webScrap():
    """Recibe desde la ruta una direccion web
    Retorna  el texto de la direccion"""
    url = request.args.get('url')
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'html.parser')
    text = ""
    for paragraph in soup.find_all('p'):
        text = text + paragraph.getText()
    text = text.replace("\n","")
    text = text.replace("\"", "'")
    return jsonify(text)


@app.route('/2a/', methods=['GET'])
def get_texto():
    """Recibe desde la ruta un texto.
    Retorna una lista de listas con las palabras de cada parrafo en ellas."""
    texto = request.args.get('texto')                       #type: str
    #parrafos = [s.strip() for s in texto.splitlines()]
    parrafos = nltk.sent_tokenize(texto)                    #type: list
    size = len(parrafos)
    for x in range(size):
        #aux = parrafos[x].split()
        aux = nltk.word_tokenize(parrafos[x])
        parrafos[x] = aux                                   #type: list[list[str]]

    return jsonify(parrafos)


@app.route('/3a/', methods=['GET'])
def lowerCase():
    """Recibe desde la ruta una lista de listas con texto
    Retorna una lista de listas con todo el texto en minuscula"""
    parameter = request.args.get('value')
    list = ast.literal_eval(parameter)
    for x in range(len(list)):
        list[x] = list[x][0].lower()

    return jsonify(list)


@app.route('/4a/', methods=['GET'])
def get_listas():
    """Recibe desde la ruta una lista de listas con strings desordenados.
    Retorna una lista de listas con los strings ordenados alfabeticamente."""

    str = request.args.get('listas')        #type: str
    list = ast.literal_eval(str)            #type: list[list[str]]

    size = len(list)
    for x in range(size):
        aux = sorted(list[x])
        list[x] = aux
    return jsonify(list)


if __name__ == "__main__":
    """Inicia la ejecución del servidor."""
    app.run(host='127.0.0.1', port=5000, debug=True)
