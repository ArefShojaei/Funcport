import pytest
from funcport import string

@pytest.mark.parametrize("text, expected", [
    ("Aref", "aref"),
    ("Car", "car"),
    ("This is my name", "this is my name")
])
def test_convert_first_string_character_to_lowercase(text: str, expected: str):
    new_text = string.lcfirst(text)

    assert new_text[0] != text[0]
    assert new_text == expected