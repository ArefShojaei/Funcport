import pytest
from funcport import string
from typing import Any


@pytest.mark.parametrize("text, find, replace, expected", [
    ("Hello world", "world", "Aref", "Hello Aref"),
    ("I can call you now", "can", "must", "I must call you now"),
    ("Python is a programming language", "is a", "is an awesome", "Python is an awesome programming language")
])
def test_replace_string(text: str, find: str, replace: str, expected: str):
    value = string.replace(text, find, replace)

    assert value == expected

@pytest.mark.parametrize("text, find, replace, expected_exception, expected_message", [
    # Text
    (["list"], "world", "Aref", TypeError, "text should be string!"),
    (("tuple",), "world", "Aref", TypeError, "text should be string!"),
    ({"dict" : []}, "world", "Aref", TypeError, "text should be string!"),
    (1, "world", "Aref", TypeError, "text should be string!"),
    (3.14, "world", "Aref", TypeError, "text should be string!"),
    (True, "world", "Aref", TypeError, "text should be string!"),
    (False, "world", "Aref", TypeError, "text should be string!"),

    # Find
    ("Hello world", ["list"], "Aref", TypeError, "find should be string!"),
    ("Hello world", ("tuple",), "Aref", TypeError, "find should be string!"),
    ("Hello world", {"dict" : []}, "Aref", TypeError, "find should be string!"),
    ("Hello world", 1, "Aref", TypeError, "find should be string!"),
    ("Hello world", 3.14, "Aref", TypeError, "find should be string!"),
    ("Hello world", True, "Aref", TypeError, "find should be string!"),
    ("Hello world", False, "Aref", TypeError, "find should be string!"),

    # Replcae
    ("Hello world", "world", ["list"], TypeError, "replace should be string!"),
    ("Hello world", "world", ("tuple",), TypeError, "replace should be string!"),
    ("Hello world", "world", {"dict" : []}, TypeError, "replace should be string!"),
    ("Hello world", "world", 1, TypeError, "replace should be string!"),
    ("Hello world", "world", 3.14, TypeError, "replace should be string!"),
    ("Hello world", "world", True, TypeError, "replace should be string!"),
    ("Hello world", "world", False, TypeError, "replace should be string!"),

])
def test_repeat_validation(text: Any, find: Any, replace: Any, expected_exception: object, expected_message: str):
    with pytest.raises(expected_exception) as error:
        string.replace(text, find, replace)

    assert str(error.value) == expected_message

def test_replace_string_with_invalid_input():
    text = "Hello world"
    find = "World"
    replace = "Aref"
    
    assert string.replace(text, find, replace) == None
