from our_store.models import User
from flask import g, current_app


def get_db():
    config = current_app.config



class UserAdapter:
    def __init__(self, adapter):
        self.adapter = adapter

    def get(self, _id: int):
        self.adapter.cursor.execute("SELECT id, name, email from users where %s", (_id,))
        return User(*self.cursor.fetch_one())


class DatabaseAdapter:
    def __init__(self, connection):
        self.con = connection
        self.cursor = self.con.cursor()
        self.users = UserAdapter(self)


db_adapter.users.get(1)
