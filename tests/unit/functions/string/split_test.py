import pytest
from funcport import string


@pytest.mark.parametrize("text, expected", [
    ("Hello", ["H", "e", "l", "l", "o"]),
    ("Dev", ["D", "e", "v"]),
    ("Unit test", ["U", "n", "i", "t", " ", "t", "e", "s", "t"])
])
def test_split_string(text: str, expected: list):
    list = string.split(text)

    assert list == expected
    assert type(list) == type(expected)
    assert list is not expected