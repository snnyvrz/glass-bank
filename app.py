import json

from flask import Flask, jsonify

app = Flask(__name__)

# loading mock data
with open('./MOCK_DATA.json') as json_file:
    products = json.load(json_file)


@app.route("/products")
def hello():
    return jsonify(products)


app.run()
