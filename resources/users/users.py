import json
from datetime import timedelta

from flask import request
from flask_jwt_extended import create_access_token
from flask_restx import Resource, Namespace

from database.users.users import User
from .decorators import authenticate
from .parser import user_post_parser, me_get_parser
from .schema import UserSchema

api = Namespace("users")


class UserApi(Resource):
    @api.expect(user_post_parser)
    def post(self):
        try:
            data = user_post_parser.parse_args()
            email = data["email"]
            password = data["password"]

            # check if email already exists
            if User.objects(email=email).first():
                return {"message": "Email already exists"}, 400

            # create new user
            user = User(email=email, password=password)
            user.generate_hash_password()
            user.save()

            user_id = user.id
            return {"message": "User created successfully", "user_id": str(user_id)}, 201
        except Exception as e:
            return {"message": f"Something went wrong -- {str(e)}"}, 500


class LoginApi(Resource):
    @api.expect(user_post_parser)
    def post(self):
        try:
            data = user_post_parser.parse_args()
            email = data["email"]
            password = data["password"]

            # check if email exists
            user = User.objects(email=email).first()
            if not user:
                return {"message": "Email does not exist"}, 400

            # check if password is correct
            if not user.check_hash_password(password):
                return {"message": "Password is incorrect"}, 400

            expires = timedelta(days=1)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {"token": access_token}, 200
        except Exception as e:
            return {"message": f"Something went wrong -- {str(e)}"}, 500


class MeApi(Resource):
    @api.expect(me_get_parser)
    @authenticate
    def get(self):
        try:
            user = request.user
            user_schema = UserSchema()
            user = user_schema.dump(user)
            return {"user": user}, 200
        except Exception as e:
            return {"message": f"Something went wrong -- {str(e)}"}, 500
