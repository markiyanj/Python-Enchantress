from flask import Blueprint, url_for


main = Blueprint('main', __name__)


@main.route('/main')
def hello():
    return url_for('auth.blah')
