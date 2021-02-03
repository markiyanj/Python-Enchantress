Implement python CRUD functions for shop database and cover it with
integration tests (database connection included) positive and negative
cases (good luck :)

Tests should be in separate module.

CRUD for cart and cart details should be done together
  `create_cart(dict: cart)` where cart
  `{'user_id': 1, 'creation_time': datetime(...), 'cart_details': [DICTS_WITH_CART_DETAILS]...}`

# create and test next functions
* `create_user(dict: user_info)`
* `read_user_info(int: _id)`
* `update_user(dict: new_info, int: _id`
* `delete_user(int: _id)`
* `create_cart(dict: cart)`
* `update_cart(dict: cart)`
* `read_cart(int: _id)`
* `delete_cart(int: _id)` - should delete cart_details as well
