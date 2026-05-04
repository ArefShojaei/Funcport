import pytest
from funcport import string

@pytest.mark.parametrize("text, expected", [
    ("AREF", "aref"),
    ("CAR", "car"),
    ("THIS IS MY NAME", "this is my name")
])
def test_string_characters_to_lowercase(text: str, expected: str):
    new_text = string.lcwords(text)

    assert new_text[0] != text[0]
    assert new_text == expected