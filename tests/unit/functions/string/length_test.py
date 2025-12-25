import pytest
from funcport import string
from typing import Any


@pytest.mark.parametrize("text, expected", [
    ("Hello", 5),
    ("Python", 6),
    ("Ext", 3),
    (".", 1),
    ("", 0),
])
def test_get_string_length(text: str, expected: int):
    length = string.length(text)

    assert length == expected

@pytest.mark.parametrize("input", [
    None, 
    123, 
    45.67, 
    ["list"], 
    {"dict": 1}, 
    {"set"}, 
    b"bytes", 
    True, 
    False, 
    lambda x: x, 
    object()
])
def test_get_string_length_with_invalid_input(input: Any):
    with pytest.raises(TypeError) as error:
        string.length(input)

    assert str(error.value) == "text should be string!"