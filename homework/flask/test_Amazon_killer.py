from freezegun import freeze_time
from Amazon_killer import amazon_killer as app
import pytest


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_crud_user(store_app):
    # create user test
    response = store_app.post(
        '/users',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@gmail.com",
        })
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
        "registration_timestamp": '2021-02-08T14:16:41'
    }
    user_id = response.json['user_id']

    # get user`s info test
    response = store_app.get(f'/users/{user_id}')

    assert response.status_code == 200
    assert response.json == {
        "name": "Illia",
        "email": "illia.sukonnik@gmail.com",
        "user_id": user_id,
        "registration_timestamp": '2021-02-08T14:16:41',
    }

    # update user`s info test
    new_user_info = {
        "name": "Illia",
        "email": "illia.sukonnik@example.com",
    }

    response = store_app.put(f'/users/{user_id}', json=new_user_info)

    assert response.status_code == 200
    assert response.json == {"status": "success"}

    # delete user`s info test
    response = store_app.delete(f'/users/{user_id}')

    assert response.status_code == 200
    assert response.json == {"status": "success"}


def test_get_user_no_such_user(store_app):
    # create new user to get last id
    response = store_app.post(
        '/users',
        json={
            "name": "test",
            "email": "test",
        })
    user_id = response.json['user_id']

    response = store_app.get(f'/users/{user_id + 1}')

    assert response.status_code == 404
    assert response.json == {
        "error": "no such user with id 1"
    }


@freeze_time('2021-02-08 14:16:41')
def test_crud_cart(store_app):
    # create cart
    create_cart_info = {
        "user_id": 1,
        "products": [
            {
                "product": 'Book: how to stop be boring',
                "price": 500,
            },
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }
    response = store_app.post('/carts', json=create_cart_info)

    assert response.status_code == 201
    assert response.json == {
        "cart_id": 1,
        "creation_time": '2021-02-08T14:16:41'
    }

    cart_id = response.json['cart_id']

    # get cart info
    response = store_app.get(f'/carts/{cart_id}')

    assert response.status_code == 200
    assert response.json == {
        "user_id": 1,
        "creation_time": '2021-02-08T14:16:41',
        "products": [
            {
                "product": 'Book: how to stop be boring',
                "price": 500,
            },
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }

    # update cart info
    cart_update_info = {
        "user_id": 1,
        "products": [
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }

    response = store_app.put(f'/carts/{cart_id}', json=cart_update_info)

    assert response.status_code == 200
    assert response.json == {"status": "success"}

    # delete cart

    response = store_app.delete(f'/carts/{cart_id}')

    assert response.status_code == 200
    assert response.json == {"status": "success"}


def test_get_cart_no_such_cart(store_app):
    # create new cart to get last id
    response = store_app.post(
        '/carts',
        json={
            "user_id": 1,
            "products": [
                {
                    "product": 'Book: how to stop be boring',
                    "price": 500,
                },
                {
                    "product": 'fireworks',
                    "price": 1500,
                }
            ]
        })
    cart_id = response.json['cart_id']

    response = store_app.get(f'/carts/{cart_id + 1}')

    assert response.status_code == 404
    assert response.json == {
        "error": "no such cart with id 1"
    }
