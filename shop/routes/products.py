from flask import Blueprint
from shop.product.models import Product
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from shop.product.models import Product
from shop.db import db
from shop.user.decorators import admin_required

product_bp = Blueprint("products", __name__)
api = Api(product_bp)


resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Float,
    "quantity": fields.Integer,
}


class Products(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "name", type=str, required=True, help="No name provided"
        )
        self.reqparse.add_argument(
            "price",
            type=float,
            required=True,
            help="No price provided",
        )
        self.reqparse.add_argument(
            "quantity",
            type=int,
            required=True,
            help="No quantity provided",
        )
        super().__init__()

    def get(self):
        return Product.query.all()

    @marshal_with(resource_fields)
    @admin_required()
    def post(self):
        data = self.reqparse.parse_args()
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product, 201


api.add_resource(Products, "/products", methods=["GET", "POST"])
