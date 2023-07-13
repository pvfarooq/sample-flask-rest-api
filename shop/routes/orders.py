from flask_restful import Resource, Api
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from shop.orders.models import Order

order_bp = Blueprint("order", __name__)
api = Api(order_bp)


class OrderResource(Resource):
    def __init__(self):
        super().__init__()


class OrderListResource(OrderResource):
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        Order.query.filter_by(user_id=user["id"]).all()
        return "OrderListResource"


api.add_resource(OrderListResource, "/orders")
