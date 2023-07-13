from shop.db import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    is_completed = db.Column(db.Boolean, default=False)


class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer, nullable=False)
