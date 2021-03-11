import click
from flask_login import LoginManager
from flask.cli import AppGroup
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
user_cli = AppGroup('user')
login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))


@app.cli.command('create-db')
def create_db():
    db.create_all()


@user_cli.command('create')
@click.argument('name')
@click.argument('email')
def add_user(name, email):
    print(current_app.config)
    db.session.add(User(username=name, email=email))
    db.session.commit()


app.cli.add_command(user_cli)


if __name__ == '__main__':
    db.session.commit()

    print(User.query.all())
