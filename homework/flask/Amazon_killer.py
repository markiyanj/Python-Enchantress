from flask import Flask, request
from datetime import datetime

amazon_killer = Flask(__name__)

USERS_DATABASE = {}
user_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {"error": "no such user with id 1"}, 404


@amazon_killer.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


if __name__ == '__main__':
    amazon_killer.run(debug=True)
