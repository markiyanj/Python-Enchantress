from our_store.store import my_store


def test_store():
    assert my_store() == "hello"
