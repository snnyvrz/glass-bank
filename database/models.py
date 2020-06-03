from .db import db


class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    category = db.IntField(required=True)
    creation_date = db.StringField(required=True)
    price = db.StringField(required=True)
