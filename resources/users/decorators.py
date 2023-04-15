from flask import request
from flask_jwt_extended import decode_token

from database.users.users import User


def authenticate(func):
    def wrapper(*args, **kwargs):
        try:
            token = request.headers.get('access-token')

            # empty token
            if not token:
                return {"message": "Access Token is missing"}, 400

            user_id = decode_token(token)['sub']

            # check user exists
            user = User.objects(id=user_id).first()
            if not user:
                return {"message": "Invalid Access Token"}, 400

            # store user in request
            request.user = user

        except Exception as e:
            return {"message": f"Something went wrong -- {str(e)}"}, 400

        return func(*args, **kwargs)

    return wrapper
