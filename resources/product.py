from flask import request, Response

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from database.models import Product, User


class ProductsApi(Resource):
    def get(self):
        products = Product.objects().to_json()
        return Response(products, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        product = Product(**body, added_by=user)
        product.save()
        user.update(push__products=product)
        user.save()
        return {'id': str(product.id)}, 200


class ProductApi(Resource):
    def get(self, id):
        product = Product.objects.get(id=id).to_json()
        return Response(product, mimetype="application/json", status=200)

    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        Product.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Product.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        product = Product.objects.get(id=id, added_by=user_id)
        product.delete()
        return '', 200
