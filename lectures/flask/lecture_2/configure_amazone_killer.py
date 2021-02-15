from flask import Blueprint, request


def before_request_for_hello():
    print("Hi I'm here")


hello = Blueprint('hello', __name__, url_prefix='/hello-bp')
hello.before_request(before_request_for_hello)

@hello.route('/hi')
def hi():
    return "hi from blueprint"


another_hello = Blueprint('another', __name__, url_prefix='/another')
@another_hello.route('/aloha')
def aloha():
    return "aloha from blueprint"
