import pytest
from funcport import string


@pytest.mark.parametrize("text, length, expected", [
    ("Hello", 2, "HelloHello"),
    ("Bye ", 3, "Bye Bye Bye "),
])
def test_repeat_string(text: str, length: int, expected: str):
    value = string.repeat(text, length)

    assert value == expected