from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL


url = URL(
    drivername='postgresql+psycopg2',
    username='illia',
    password='pass',
    host='localhost',
    port=5432,
    database='illia'
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    user = db.relationship('User', backref=db.backref('carts', lazy=True), cascade="all, delete", passive_deletes=True)


class CartDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id', ondelete="CASCADE"), nullable=False)
    cart = db.relationship('Cart', backref=db.backref('products', lazy=True), cascade="all, delete", passive_deletes=True)




@app.route('/')
def users():
    return User.query.all()


if __name__ == '__main__':
    db.create_all()
    illia = User(username='Illia', email='illia.sukonnik@gmail.com')
    student = User(username='Some Student', email='some.student@example.com')

    db.session.add(illia)
    db.session.add(student)

    illias_cart = Cart(user=illia)
    illias_cart.products = [
        CartDetails(product_name='showel', price=100),
        CartDetails(product_name='ski', price=200),
    ]
    db.session.commit()

    app.run()
