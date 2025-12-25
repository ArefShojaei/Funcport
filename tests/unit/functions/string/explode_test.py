import pytest
from funcport import string


@pytest.mark.parametrize("text, separator, expected", [
    ("Hello world", " ", ["Hello", "world"]),
    ("Python unit test", " ", ["Python", "unit", "test"])
])
def test_explode_string_to_list(text: str, separator: str, expected: list):
    list = string.explode(separator, text)

    assert list == expected
    assert type(list) == type(expected)
    assert list is not expected