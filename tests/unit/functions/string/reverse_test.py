import pytest
from funcport import string

@pytest.mark.parametrize("text, expected", [
    ("Hello", "olleH"),
    ("This is my name", "eman ym si sihT"),
    ("123", "321"),
    ("NULL", "LLUN"),
])
def test_reverse_string(text: str, expected: str):
    reversed_text = string.reverse(text)

    assert reversed_text != text
    assert reversed_text == expected
    assert len(reversed_text) == len(expected)