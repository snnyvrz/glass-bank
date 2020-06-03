from flask import Flask, request, Response

from database.db import initialize_db
from database.models import Product


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/glass-bank'
}

initialize_db(app)


@app.route("/products")
def get_products():
    products = Product.objects().to_json()
    return Response(products, mimetype="application/json", status=200)


@app.route("/products", methods=['POST'])
def add_product():
    body = request.get_json()
    product = Product(**body).save()
    return {'id': str(product.id)}, 200


@app.route("/products/<id>")
def get_product(id):
    product = Product.objects.get(id=id).to_json()
    return Response(product, mimetype="application/json", status=200)


@app.route("/products/<id>", methods=['PUT'])
def update_product(id):
    body = request.get_json()
    Product.objects.get(id=id).update(**body)
    return '', 200


@app.route("/products/<id>", methods=['DELETE'])
def delete_product(id):
    Product.objects.get(id=id).delete()
    return '', 200


app.run()
