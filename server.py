# Authors: Meyer Montagner, Pablo Villalba
# Programa que inicia un servidor usado como práctica del concepto de API.

from typing import Dict
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import urllib.request
import ast

app = Flask(__name__)                           # type: Flask



@app.route('/1a/', methods=['GET'])
def webScrap():
    url = request.args.get('url')
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage, 'html.parser')
    text = ""
    for paragraph in soup.find_all('p'):
        text = text + paragraph.getText()
    text = text.replace("\n","")
    text = text.replace("\"", "'")
    return jsonify(text)


@app.route('/3a/')
def lowerCase():
    parameter = request.args.get('value')
    list = ast.literal_eval(parameter)
    for x in range(len(list)):
        list[x] = list[x][0].lower()

    return jsonify(list)



if __name__ == "__main__":

    """Inicia la ejecución del servidor."""
    app.run(host='127.0.0.1', port=5000, debug=True)