from flask import request, Response

from flask_restful import Resource

from database.models import Product


class ProductsApi(Resource):
    def get(self):
        products = Product.objects().to_json()
        return Response(products, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        product = Product(**body).save()
        return {'id': str(product.id)}, 200


class ProductApi(Resource):
    def get(self, id):
        product = Product.objects.get(id=id).to_json()
        return Response(product, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Product.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Product.objects.get(id=id).delete()
        return '', 200
