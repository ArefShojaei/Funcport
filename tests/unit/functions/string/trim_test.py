import pytest
from funcport import string
from typing import Any


@pytest.mark.parametrize("text, expected", [
    (" Hello ", "Hello"),
    (" Hello world ", "Hello world"),
    (" Hello from Python! ", "Hello from Python!"),
])
def test_remove_string_whitespace_both_side(text: str, expected: str):
    assert string.trim(text) == expected
    assert type(string.trim(text)) == type(string.trim(text))
    assert len(text) != len(expected)

@pytest.mark.parametrize("text, expected", [
    (" Hello", "Hello"),
    (" Hello world", "Hello world"),
    (" Hello from Python!", "Hello from Python!"),
])
def test_remove_string_whitespace_only_left_side(text: str, expected: str): pass

@pytest.mark.parametrize("text, expected", [
    ("Hello ", "Hello"),
    ("Hello world ", "Hello world"),
    ("Hello from Python! ", "Hello from Python!"),
])
def test_remove_string_whitespace_only_right_side(text: str, expected: str): pass

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
def test_remove_string_whitespace_with_invalid_input(input: Any):
    with pytest.raises(TypeError) as error : 
        string.trim(input)

    assert str(error.value) == "Invalid input data type!"