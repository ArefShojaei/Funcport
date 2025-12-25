import pytest
from funcport import string


@pytest.mark.parametrize("text, length, expected", [
    ("Hello", 2, "HelloHello"),
    ("Bye ", 3, "Bye Bye Bye "),
])
def test_repeat_string(text: str, length: int, expected: str):
    value = string.repeat(text, length)

    assert value == expected

@pytest.mark.parametrize("text, length, expected_exception, expected_message", [
    # Text -> ValueError
    ("", 5, ValueError, "text should not be empty!"),
    ("", 1, ValueError, "text should not be empty!"),
    ("", 100, ValueError, "text should not be empty!"),

    # Length -> ValueError
    ("hello", 0, ValueError, "length should not be zero or negative!"),
    ("hello", -5, ValueError, "length should not be zero or negative!"),

    # Text -> TypeError
    (123, 5, TypeError, "text should be string!"),
    (None, 5, TypeError, "text should be string!"),
    ([], 3, TypeError, "text should be string!"),

    # Length -> TypeError
    ("hello", 3.14, TypeError, "length should be int!"),
    ("hello", "5", TypeError, "length should be int!"),
    ("hello", None, TypeError, "length should be int!"),
])
def test_repeat_empty_string(text: str, length: int, expected_exception: object, expected_message: str):
    with pytest.raises(expected_exception) as error:
        string.repeat(text, length)

    assert str(error.value) == expected_message