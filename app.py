from flask import Flask
from flask_restx import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.extensions import ma, bcrypt, jwt, api, celery

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
celery.conf.update(app.config)

api.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
ma.init_app(app)

initialize_db(app)
initialize_routes(api)
