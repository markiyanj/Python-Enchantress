from flask import Flask
from flask_restful import Api
from our_store.resourses import Users


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('./config.py')
    api = Api(app)
    api.add_resource(Users, "/users", "/users/<int:user_id>")
    return app
