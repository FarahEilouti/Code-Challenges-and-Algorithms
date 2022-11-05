# Write your test here
from challenge02 import is_valid

def test_challenge():

    result = is_valid(string="()")

    actual = result
    expected = True
    assert actual == expected

def test2_challenge():

    result = is_valid(string="({)")

    actual = result
    expected = False
    assert actual == expected


