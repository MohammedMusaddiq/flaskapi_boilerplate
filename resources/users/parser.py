from flask_restx import reqparse

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument("email", type=str, required=True, location="json", help="Email is required")
user_post_parser.add_argument("password", type=str, required=True, location="json", help="Password is required")

me_get_parser = reqparse.RequestParser()
me_get_parser.add_argument("access-token", type=str, required=True, location="headers", help="access-token is required")
