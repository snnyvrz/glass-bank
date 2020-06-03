from flask import Blueprint, request, Response

from database.models import Product

products = Blueprint('products', __name__)


@products.route("/products")
def get_products():
    products = Product.objects().to_json()
    return Response(products, mimetype="application/json", status=200)


@products.route("/products", methods=['POST'])
def add_product():
    body = request.get_json()
    product = Product(**body).save()
    return {'id': str(product.id)}, 200


@products.route("/products/<id>")
def get_product(id):
    product = Product.objects.get(id=id).to_json()
    return Response(product, mimetype="application/json", status=200)


@products.route("/products/<id>", methods=['PUT'])
def update_product(id):
    body = request.get_json()
    Product.objects.get(id=id).update(**body)
    return '', 200


@products.route("/products/<id>", methods=['DELETE'])
def delete_product(id):
    Product.objects.get(id=id).delete()
    return '', 200
