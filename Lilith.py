#coding=utf-8
import os
from flask import Flask, request, jsonify, json

from Kroni import seek_and_destroy

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    if request.method == 'GET':
        json_output = seek_and_destroy("DY575086091BR")
        return json_output


@app.route('/rastreamento', methods=['POST'])
def rastreamento():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            d = json.loads(request.data)
            cod = (d['cod'])
            json_output = seek_and_destroy(cod)

            return json_output


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
