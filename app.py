from flask import Flask

from database.db import initialize_db
from resources.product import Products


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/glass-bank'
}

initialize_db(app)

app.register_blueprint(Products)

app.run()
