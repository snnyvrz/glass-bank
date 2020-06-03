from flask_bcrypt import generate_password_hash, check_password_hash

from .db import db


class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    category = db.IntField(required=True)
    creation_date = db.StringField(required=True)
    price = db.StringField(required=True)


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
