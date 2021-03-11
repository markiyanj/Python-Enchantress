from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


fishes_in_lakes = db.Table(
    'fishes_in_lakes',
    db.Column('fish_id', db.Integer, db.ForeignKey('fishes.id')),
    db.Column('lake', db.Integer, db.ForeignKey('lakes.id')),
)


class Fish(db.Model):
    __tablename__ = 'fishes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    lakes = db.relationship(
        'Lake',
        secondary=fishes_in_lakes,
        backref='fishes'
    )

class Lake(db.Model):
    __tablename__ = 'lakes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)



db.create_all()
tuna = Fish(name='Tuna')
db.session.add(tuna)
baikal = Lake(name='baikal')

tuna.lakes.append(baikal)

db.session.commit()
