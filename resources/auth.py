import datetime

from flask import request

from flask_jwt_extended import create_access_token
from flask_restful import Resource

from database.models import User


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        return {'id': str(user.id)}, 200


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or Password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
