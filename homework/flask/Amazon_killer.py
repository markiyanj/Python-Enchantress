from flask import Flask, request
from datetime import datetime

amazon_killer = Flask(__name__)

USERS_DATABASE = {}
CARTS_DATABASE = {}


class Users:
    user_id = 0

    def __init__(self):
        Users.user_id += 1


class Carts:
    cart_id = 0

    def __init__(self):
        Carts.cart_id += 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    new_user = Users()
    user = request.json
    user['user_id'] = new_user.user_id
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": new_user.user_id
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[new_user.user_id] = user

    return response, 201


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {"error": "no such user with id 1"}, 404


@amazon_killer.route('/users/<int:user_id>', methods=["PUT"])
def update_user_info(user_id):
    new_user_info = request.json
    try:
        user = USERS_DATABASE[user_id]

        user['name'] = new_user_info['name']
        user['email'] = new_user_info['email']

        USERS_DATABASE[user_id] = user

        response = {"status": "success"}
        return response, 200

    except KeyError:
        raise NoSuchUser


@amazon_killer.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amazon_killer.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        USERS_DATABASE.pop(user_id)
        response = {"status": "success"}

        return response, 200

    except KeyError:
        raise NoSuchUser


@amazon_killer.route('/carts', methods=['POST'])
def create_cart():
    new_cart = Carts()
    cart = request.json
    cart['user_id'] = new_cart.cart_id
    response = {
        "cart_id": new_cart.cart_id,
        "creation_time": datetime.now().isoformat()
    }

    cart["creation_time"] = response['creation_time']
    CARTS_DATABASE[new_cart.cart_id] = cart

    return response, 201


@amazon_killer.errorhandler(NoSuchCart)
def no_such_cart_handler(e):
    return {"error": "no such cart with id 1"}, 404


@amazon_killer.route('/carts/<int:cart_id>')
def get_cart(cart_id):
    try:
        cart = CARTS_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@amazon_killer.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart_info(cart_id):
    new_cart_info = request.json
    try:
        cart = CARTS_DATABASE[cart_id]

        cart['products'] = new_cart_info['products']

        CARTS_DATABASE[cart_id] = cart

        response = {"status": "success"}
        return response, 200

    except KeyError:
        raise NoSuchUser


@amazon_killer.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart_info(cart_id):
    try:
        CARTS_DATABASE.pop(cart_id)
        response = {"status": "success"}

        return response, 200

    except KeyError:
        raise NoSuchCart


if __name__ == '__main__':
    amazon_killer.run(debug=True)
