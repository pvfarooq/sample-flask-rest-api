from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

jwt = JWTManager()


def generate_access_token(user):
    additional_claims = {"username": user.username, "role": user.role}
    access = create_access_token(identity=user.id, additional_claims=additional_claims)
    return access


def generate_refresh_token(user):
    refresh = create_refresh_token(identity=user.id)
    return refresh


def generate_tokens(user):
    return {
        "access": generate_access_token(user),
        "refresh": generate_refresh_token(user),
    }
