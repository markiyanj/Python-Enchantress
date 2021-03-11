import click
from flask.cli import AppGroup
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
user_cli = AppGroup('user')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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
