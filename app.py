import json

from flask import Flask, jsonify, request

app = Flask(__name__)

# loading mock data
with open('./MOCK_DATA.json') as json_file:
    products = json.load(json_file)


@app.route("/products")
def get_products():
    return jsonify(products)


@app.route("/products", methods=['POST'])
def add_product():
    product = request.get_json()
    products.append(product)
    return {'id': len(products)}, 200


@app.route("/products/<int:id>", methods=['GET'])
def get_product(id):
    return jsonify(products[id - 1]), 200


@app.route("/products/<int:id>", methods=['PUT'])
def update_product(id):
    product = request.get_json()
    index = id - 1
    products[index] = product
    return jsonify(products[index]), 200


@app.route("/products/<int:id>", methods=['DELETE'])
def deleye_product(id):
    index = id - 1
    del products[index]
    return 'None', 200


app.run()
