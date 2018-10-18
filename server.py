# Developers: Meyer Montagner, Pablo Villalba
# Scrum Manager: Damaso
# Programa que inicia un servidor usado como práctica de Scrum.


from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import urllib.request
import ast
import nltk


app = Flask(__name__)                           # type: Flask


@app.route('/1a/', methods=['GET'])
def webScrap():
    """Recibe desde la ruta una lista de listas con.
    Retorna una lista de listas con."""
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
    """Recibe desde la ruta una lista de listas con.
    Retorna una lista de listas con."""
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