import unittest

from application.server import compute


def test_all_users(client):
    response = client.get('/users')
    assert b'[{"email":"test@mail.fr","user_data":["1010101","00220020"]},{"email":"u2@mail.fr","user_data":["11111"]}]' in response.data


class TestUsers(unittest.TestCase):

    def test_compute(self):
        self.assertEquals(compute(1, 1), 2)
