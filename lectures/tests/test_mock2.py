import unittest
from unittest import mock
import os


def read_from_file():
    res = os.listdir()
    return res


def reader():
    res = read_from_file()
    if '1.txt' in res:
        return True


class TestRead(unittest.TestCase):

    @mock.patch("os.listdir", mock.Mock(return_value=['1.txt', '2.txt', '3.txt']))
    def test_read_from_file(self):
        self.assertEqual(reader(), ['1.txt', '2.txt', '3.txt'])


if __name__ == "__main__":
    unittest.main()
