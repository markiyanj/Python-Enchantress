from flask import Blueprint, request


hello_bp = Blueprint('hello', __name__, url_prefix='/hello')


@hello_bp.route('/hi-there')
def hi_there():
    return "Hi there"


@hello_bp.route('/personal_hi', methods=['POST'])
def hi_name():
    name = request.json['name']
    return f"Hi {name}"
