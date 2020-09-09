import pytest
import requests


def test_check_main_page():
    """ Just check that website works as usual. """

    res = requests.get('https://www.iwebtool.com')
    assert res.status_code == 200
