import pytest
from funcport import string


@pytest.mark.parametrize("text, expected", [
    ("Hello", 5),
    ("Python", 6),
    ("Ext", 3),
    (".", 1),
])
def test_get_string_length(text: str, expected: int):
    length = string.length(text)

    assert length == expected