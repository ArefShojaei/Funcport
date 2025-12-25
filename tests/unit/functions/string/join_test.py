import pytest
from funcport import string
from typing import Any


@pytest.mark.parametrize("wordList, separator, expected", [
    (["a", "b", "c"], "*", "a*b*c"),
    (["Hello", "world"], " ", "Hello world")
])
def test_join_list_of_string_to_string(wordList: list, separator: str, expected: str):
    value = string.join(separator, wordList)

    assert value == expected

@pytest.mark.parametrize("separator, input, expected_exception, expected_message", [
    # Separator -> TypeError
    (1, ["a", "b", "c"], TypeError, "separator should be string!"),
    (3.14, ["a", "b", "c"], TypeError, "separator should be string!"),
    (["list"], ["a", "b", "c"], TypeError, "separator should be string!"),
    (("tuple",), ["a", "b", "c"], TypeError, "separator should be string!"),
    ({"dict": []}, ["a", "b", "c"], TypeError, "separator should be string!"),
    (True, ["a", "b", "c"], TypeError, "separator should be string!"),
    (False, ["a", "b", "c"], TypeError, "separator should be string!"),

    # # Separator -> ValueError
    ("", ["a", "b", "c"], ValueError, "separator can not be empty!"),

    # # Input -> TypeError
    ("*", 1, TypeError, "input should be list of string!"),
    ("*", 3.14, TypeError, "input should be list of string!"),
    ("*", ("tuple",), TypeError, "input should be list of string!"),
    ("*", {"dict": []}, TypeError, "input should be list of string!"),
    ("*", True, TypeError, "input should be list of string!"),
    ("*", False, TypeError, "input should be list of string!"),

    # # Input -> ValueError
    ("*", ["a"], ValueError, "input size can not be less than 2!"),
    ("*", [1, 2], ValueError, "each input data should be string!"),
])
def test_join_validation(separator: Any, input: Any, expected_exception: object, expected_message: str):
    with pytest.raises(expected_exception) as error:
        string.join(separator, input)

    assert str(error.value) == expected_message