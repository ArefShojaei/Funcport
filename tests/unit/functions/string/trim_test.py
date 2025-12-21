import pytest
from funcport import string


@pytest.mark.parametrize("text, expected", [
    (" Hello ", "Hello"),
    (" Hello", "Hello"),
    ("Hello ", "Hello"),

    (" Hello world ", "Hello world"),
    (" Hello world", "Hello world"),
    ("Hello world ", "Hello world"),
])
def test_trim_whitespace(text: str, expected: str):
    value = string.trim(text)

    assert value != text
    assert value == expected

def test_trim_empty_sring():
    text = ""

    value = string.trim(text)

    assert value == text    

def test_trim_no_change():
    text = "Hello"

    value = string.trim(text)

    assert value == text
