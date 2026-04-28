import pytest
from funcport import string

@pytest.mark.parametrize("first_text, second_text, expected", [
    ("Hello", " World", "Hello World"),
    ("Class", "es", "Classes"),
    ("Class", "es", "Classes"),
])
def test_concat_two_string_together(first_text: str, second_text: str, expected: str):
    value = string.concat(first_text, second_text)

    assert value == expected
    assert type(value) == type(expected)
