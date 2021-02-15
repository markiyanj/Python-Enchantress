from dataclasses import dataclass
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with


app = Flask(__name__)
api = Api(app)


@dataclass
class User:
    name: str
    surname: str
    beloved_numbers: list


user_fields = {
    'first_name': fields.String(attribute='name'),
    'surname': fields.String(),
    'beloved_numbers': fields.List(fields.Integer)
}

class Users(Resource):
    @marshal_with({
        'first_name': fields.String(attribute='name'),
        'surname': fields.String(),
        'beloved_numbers': fields.List(fields.Integer)
    })
    def get(self, user_id=None):
        return User(name="Illia", surname="Sukonnik", beloved_numbers=[1,2,3])


api.add_resource(Users, '/')


if __name__ == '__main__':
    app.run(debug=True)
