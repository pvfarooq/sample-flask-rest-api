from flask import Flask
from .settings import Config
from .db import db
from .blueprint import register_routings
from .user.jwt import jwt


def create_local_db(app):
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    register_routings(app)
    jwt.init_app(app)
    return app


app = create_app()
