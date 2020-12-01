import flask
from flask import request, jsonify

app = flask.Flask(__name__)

Colors = [
    {
     'r': 255,
     'g': 255,
     'b': 0
    }
]
@app.route('/', methods=['GET'])
def home():
    return "<h1>Color archive for plick webapp</h1><p>This site is a prototype API for plick app to test api integration</p>"

@app.route('/api/v1/resources/colors/all', methods=['GET'])
def api_all():
    return jsonify(Colors)