import pytest
from funcport import string

@pytest.mark.parametrize("text, expected", [
    ("aref", "AREF"),
    ("car", "CAR"),
    ("this is my name", "THIS IS MY NAME")
])
def test_string_characters_to_uppercase(text: str, expected: str):
    new_text = string.ucwords(text)

    assert new_text[0] != text[0]
    assert new_text == expected