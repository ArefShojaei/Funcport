import pytest
from funcport import string


@pytest.mark.parametrize("text, find, replace, expected", [
    ("Hello world", "world", "Aref", "Hello Aref"),
    ("I can call you now", "can", "must", "I must call you now"),
    ("Python is a programming language", "is a", "is an awesome", "Python is an awesome programming language")
])
def test_replace_string(text: str, find: str, replace: str, expected: str):
    value = string.replace(text, find, replace)

    assert value == expected