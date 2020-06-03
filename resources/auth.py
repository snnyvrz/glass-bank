from flask import request

from flask_restful import Resource

from database.models import User


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        return {'id': str(user.id)}, 200
