from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hi', type=str, help='Put something here')
        args = parser.parse_args()
        return {'some': args}

    def post(self):
        return request.json


api.add_resource(Users, '/')


if __name__ == '__main__':
    app.run(debug=True)
