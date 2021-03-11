from flask import Blueprint, url_for


auth = Blueprint('auth', __name__)


@auth.route('/auth')
def blah():
    return url_for('main.hello')
