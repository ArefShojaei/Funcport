import pytest
from funcport import string
from typing import Any


@pytest.mark.parametrize("text, expected", [
    ("Hello", ["H", "e", "l", "l", "o"]),
    ("Dev", ["D", "e", "v"]),
    ("Unit test", ["U", "n", "i", "t", " ", "t", "e", "s", "t"])
])
def test_split_full_string_to_list(text: str, expected: list):
    assert string.split(text) == expected
    assert type(string.split(text)) == type(expected)

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
def test_split_string_to_list_with_invalid_input(input: Any):
    with pytest.raises(TypeError) as error:
        string.split(input)

    assert str(error.value) == "Invalid input data type!"

def test_split_empty_string_to_list():
    empty_text = ""
    
    assert string.split(empty_text) == []
    assert type(string.split(empty_text)) == list