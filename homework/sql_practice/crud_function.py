from datetime import datetime
from functools import wraps

import psycopg2


class Db:

    def __init__(self, database, user, password, host):
        self.database = database
        self.user = user
        self.password = password
        self.host = host

    # Create and close connection to db
    def db_connection(func):
        def wrapper(self, *args, **kwargs):
            try:
                connection = psycopg2.connect(
                    database=self.database,
                    user=self.user,
                    password=self.password,
                    host=self.host
                )
                connection.autocommit = True
                cursor = connection.cursor()

                res = func(self, cursor=cursor, *args, **kwargs)

                if connection:
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

            except (Exception, psycopg2.Error) as error:
                print("Error in connection", error)
            return res

        return wrapper

    @db_connection
    def create_user(self, cursor, **user_info):
        try:
            postgres_insert_query = """ INSERT INTO users (name, email, registration_time) 
            VALUES (%(name)s,%(email)s,%(registration_time)s)"""
            cursor.execute(postgres_insert_query, user_info)

            count = cursor.rowcount
            print(count, "Record inserted successfully into users table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into users table", error)

    @db_connection
    def get_last_user_id(self, cursor):
        cursor.execute("""SELECT id 
                            FROM users
                            ORDER BY id DESC
                            LIMIT 1""")

        _id = cursor.fetchone()
        return _id

    @db_connection
    def read_user_info(self, _id: int, cursor):
        try:
            cursor.execute("SELECT name, email, registration_time FROM users WHERE id = %s", (_id,))

            results = cursor.fetchone()
            print(results)
            return results
        except (Exception, psycopg2.Error) as error:
            print("Error in Read operation", error)

    @db_connection
    def update_user(self, cursor, **new_info):
        try:
            sql_update_query = """UPDATE users 
            SET name=%(name)s,email=%(email)s,registration_time=%(registration_time)s 
            WHERE id = %(id)s"""
            cursor.execute(sql_update_query, new_info)
            count = cursor.rowcount
            print(count, "Record Updated successfully ")
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    @db_connection
    def delete_user(self, _id, cursor):
        try:
            sql_delete_query = """DELETE FROM users WHERE id = %s"""
            cursor.execute(sql_delete_query, _id)
        except (Exception, psycopg2.Error) as error:
            print("Error in Delete operation", error)

    @db_connection
    def get_last_cart_id(self, cursor):
        cursor.execute("""SELECT id 
                            FROM cart
                            ORDER BY id DESC
                            LIMIT 1""")

        _id = cursor.fetchone()
        return _id

    @db_connection
    def create_cart(self, cursor, **cart):
        try:
            postgres_insert_cart = """ INSERT INTO cart (creation_time, user_id) 
            VALUES (%(creation_time)s,%(user_id)s)"""
            cursor.execute(postgres_insert_cart, cart)

            cart_id = self.get_last_cart_id()
            cart['cart_details']['cart_id'] = cart_id

            postgres_insert_cart_details = f""" INSERT INTO cart_details (cart_id, price, product) 
            VALUES (%(cart_id)s, %(price)s, %(product)s)"""
            cursor.execute(postgres_insert_cart_details, cart.get('cart_details'))

            count = cursor.rowcount
            print(count, "Record inserted successfully into users table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into cart table", error)

    @db_connection
    def update_cart(self, cursor, **new_info):
        try:
            sql_update_cart = """UPDATE cart 
            SET creation_time=%(creation_time)s,user_id=%(user_id)s 
            WHERE id = %(id)s"""
            cursor.execute(sql_update_cart, new_info)

            sql_update_cart_details = """UPDATE cart_details 
            SET price=%(price)s,product=%(product)s
            WHERE cart_id=%(cart_id)s"""
            cursor.execute(sql_update_cart_details, new_info.get('cart_details_update'))
            count = cursor.rowcount
            print(count, "Record Updated successfully ")
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    @db_connection
    def read_cart(self, _id, cursor):
        try:

            cursor.execute("""SELECT cart.creation_time, cart_details.product, cart_details.price 
            FROM cart 
            LEFT JOIN cart_details 
            ON cart.id=cart_details.cart_id 
            WHERE cart.id=%s;""", (_id,))

            results = cursor.fetchone()
            print(results)
            return results
        except (Exception, psycopg2.Error) as error:
            print("Error in Read operation", error)

    @db_connection
    def delete_cart(self, _id, cursor):
        try:
            sql_delete_cart_details = """DELETE FROM cart_details WHERE cart_id = %s"""
            cursor.execute(sql_delete_cart_details, _id)

            sql_delete_cart = """DELETE FROM cart WHERE id = %s"""
            cursor.execute(sql_delete_cart, _id)

        except (Exception, psycopg2.Error) as error:
            print("Error in Delete operation", error)
