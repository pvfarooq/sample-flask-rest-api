from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask import abort


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] == "admin":
                return fn(*args, **kwargs)
            else:
                abort(403)

        return decorator

    return wrapper
