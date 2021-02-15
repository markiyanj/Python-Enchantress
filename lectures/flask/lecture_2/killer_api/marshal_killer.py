from dataclasses import dataclass

from flask import Flask
from flask_restful import Resource, Api, marshal_with, fields


app = Flask(__name__)
api = Api(app)

@dataclass
class User:
    name: str
    email: str
    this_var_will_not_be_included: int

user_fields = {
    'name': fields.String,
    'email': fields.String,
}


class Users(Resource):
    @marshal_with(user_fields)
    def get(self):
        return User('Illia', 'illia.sukonnik@gmail.com', 10)


api.add_resource(Users, '/')


if __name__ == '__main__':
    app.run(debug=True)
