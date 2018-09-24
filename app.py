#coding=utf-8
import os
from flask import Response
from flask import Flask, request, jsonify, json, send_from_directory

from kroni import seek_and_destroy

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    if request.method == 'GET':
        return "DevilApi - CANSADO"


@app.route('/rastreamento', methods=['GET', 'POST'])
def rastreamento():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            d = json.loads(request.data)
            cod = (d['cod'])
            json_output = seek_and_destroy(cod)

            resp = Response(json_output, status=200, mimetype='application/json')

            return resp
        else:
            return "erro"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()
