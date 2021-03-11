from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


friends = db.Table(
    'friends',
    db.Column('first', db.Integer, db.ForeignKey('users.id')),
    db.Column('second', db.Integer, db.ForeignKey('users.id')),
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    friends = db.relationship(
        'User',
        secondary=friends,
        primaryjoin=id==friends.c.second,
        secondaryjoin=id==friends.c.first
    )
    def __repr__(self):
        return '<User %r>' % self.username

    def addfried(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)
        db.session.commit()




db.create_all()

db.session.add(User(username='Illia', email='illia.sukonnik@gmail.com'))
db.session.add(User(username='Some Student', email='some.student@example.com'))
db.session.commit()

print(User.query.all())
