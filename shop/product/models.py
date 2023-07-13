from shop.db import db
from datetime import datetime


class ProductCategory(db.Model):
    __tablename__ = "product_category"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(255), nullable=False)


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("product_category.id"), nullable=False
    )
