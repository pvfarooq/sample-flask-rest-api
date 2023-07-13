from flask import Blueprint
from flask_restful import Resource, Api, reqparse, fields
from shop.user.models import User
from ..db import db
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


from shop.user.jwt import generate_tokens, generate_access_token

user_bp = Blueprint("users", __name__)
api = Api(user_bp)


resource_fields = {
    "id": fields.Integer,
    "username": fields.String,
}


class UserResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "username", type=str, required=True, help="username is required"
        )
        self.parser.add_argument(
            "password", type=str, required=True, help="password is required"
        )
        super().__init__()


class UserRegister(UserResource):
    def post(self):
        data = self.parser.parse_args()
        username = data["username"]

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400

        password = data["password"]
        hashed_pwd = generate_password_hash(password)
        user = User(username=username, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        tokens = generate_tokens(user)
        return {
            "message": "User registered successfully",
            "access": tokens["access"],
            "refresh": tokens["refresh"],
        }, 201


class UserLogin(UserResource):
    def post(self):
        data = self.parser.parse_args()
        username = data["username"]
        password = data["password"]

        user = User.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return {"error": "invalid credentials"}, 401

        token = generate_tokens(user)
        return {"access": token["access"], "refresh": token["refresh"]}, 200


class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = generate_access_token(identity)
        return {"access": access_token}, 200


api.add_resource(UserRegister, "/user/register")
api.add_resource(UserLogin, "/user/login")
api.add_resource(RefreshToken, "/user/refresh")
