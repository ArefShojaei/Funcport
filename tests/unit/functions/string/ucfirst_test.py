import pytest
from funcport import string

@pytest.mark.parametrize("text, expected", [
    ("aref", "Aref"),
    ("car", "Car"),
    ("this is my name", "This is my name")
])
def test_convert_first_string_character_to_uppercase(text: str, expected: str):
    new_text = string.ucfirst(text)

    assert new_text[0] != text[0]
    assert new_text == expected