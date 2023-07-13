from flask import Blueprint
from shop.product.models import ProductCategory
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from shop.db import db
from flask_jwt_extended import jwt_required


product_category_bp = Blueprint("product-category", __name__)
api = Api(product_category_bp)

resource_fields = {
    "id": fields.Integer,
    "created_at": fields.DateTime,
    "title": fields.String,
}


class ProductCategoryResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title", type=str, required=True, help="this field is required"
        )
        super().__init__()

    @marshal_with(resource_fields)
    def get(self):
        return ProductCategory.query.all()

    @marshal_with(resource_fields)
    # @jwt_required()
    def post(self):
        data = self.reqparse.parse_args()
        product_category = ProductCategory(title=data["title"])
        db.session.add(product_category)
        db.session.commit()
        return product_category, 201


api.add_resource(ProductCategoryResource, "/product-category", methods=["GET", "POST"])
