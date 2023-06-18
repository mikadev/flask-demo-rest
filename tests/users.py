import unittest

import pytest

from application.server import compute


def test_all_users(client):
    response = client.get('/users')
    assert b'[{"email":"test@mail.fr","user_data":["1010101","00220020"]},{"email":"u2@mail.fr","user_data":["11111"]}]' in response.data


@pytest.mark.parametrize(
    "a,b,x",
    [
        (1, 3, 4),
        (3, 3, 6),
    ]
)
def test_add(a, b, x):
    # when
    res = compute(a, b)

    # then
    assert res == x


class TestUsers(unittest.TestCase):

    def test_compute(self):
        self.assertEquals(compute(1, 1), 2)


from unittest.mock import patch


def multi(a, b):
    return a * b


@patch('application.server.compute', side_effect=lambda a, b: a * b * 2)
def test(compute):
    res = compute(2, 2)

    # then
    assert res == 8
