from .models import User
from shop.db import db
from werkzeug.security import generate_password_hash


def create_admin(username: str, password: str):
    password = generate_password_hash(password)
    user = User(username=username, password=password, is_admin=True)
    db.session.add(user)
    db.session.commit()
    return user
