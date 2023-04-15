from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api
from celery import Celery


ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
api = Api(prefix="/api/v1", doc='/api/v1/docs')
celery = Celery(__name__, broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
