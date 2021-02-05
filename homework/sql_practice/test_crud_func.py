import datetime
import pytest
import psycopg2

from crud_function import Db

db = Db('markiian', 'markiian', '1234', 'localhost')


class TestDataBase:

    def test_crud_users(self):
        user_info = {'name': 'Marko', 'email': 'marko@gmail.com', 'registration_time': '2021-04-03 15:30:00'}

        # create new user
        db.create_user(**user_info)

        # get new user id
        last_user_id = db.get_last_user_id()

        update_user_info = {'name': 'Marek', 'email': 'marko@gmail.com', 'registration_time': '2021-04-03 15:30:00',
                            'id': last_user_id}

        # checks if the user is created correctly
        assert db.read_user_info(last_user_id) == (
            'Marko', 'marko@gmail.com', datetime.datetime(2021, 4, 3, 15, 30))

        # update user info
        db.update_user(**update_user_info)

        # checks if the user`s info is updated correctly
        assert db.read_user_info(last_user_id) == (
            'Marek', 'marko@gmail.com', datetime.datetime(2021, 4, 3, 15, 30)
        )

        # delete user
        db.delete_user(last_user_id)
        # checks if the user has been deleted
        assert db.read_user_info(last_user_id) is None

    def test_crud_cart(self):
        user_info = {'name': 'Mark', 'email': 'marko@gmail.com', 'registration_time': '2021-04-03 15:30:00'}

        # create user for cart
        db.create_user(**user_info)

        # get last user id
        user_id = db.get_last_user_id()

        cart_info = {'creation_time': '2021-04-03 15:30:00',
                     'user_id': user_id,
                     'cart_details': {
                         'cart_id': None,
                         'price': 100,
                         'product': 'kebab'
                     }}

        db.create_cart(**cart_info)

        last_cart_id = db.get_last_cart_id()

        cart_update_info = {'creation_time': '2021-04-03 15:30:00',
                            'user_id': user_id,
                            'id': last_cart_id,
                            'cart_details_update': {
                                'price': 120,
                                'product': 'big_mack',
                                'cart_id': last_cart_id
                            }}

        assert db.read_cart(last_cart_id) == (
            (datetime.datetime(2021, 4, 3, 15, 30), 'kebab', 100))

        # change cart_details info
        db.update_cart(**cart_update_info)

        # checks if the  cart info is updated correctly
        assert db.read_cart(last_cart_id) == (
            (datetime.datetime(2021, 4, 3, 15, 30), 'big_mack', 120))

        # delete cart
        db.delete_cart(last_cart_id)

        # checks if the cart has been deleted
        assert db.read_cart(last_cart_id) is None
