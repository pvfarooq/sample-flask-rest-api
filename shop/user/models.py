from shop.db import db
from datetime import datetime
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def role(self):
        if self.is_admin:
            return "admin"
        return "user"

    def check_password(self, password):
        """Check hashed password against actual password using werkzeug security"""
        return check_password_hash(self.password, password)
