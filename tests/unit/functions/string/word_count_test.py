import pytest
from funcport import string

@pytest.mark.parametrize("text, expected", [
    ("This is my new message", 5),
    ("", 1),
])
def test_count_string_words(text: str, expected: int):
    count = string.word_count(text)

    assert type(count) == int
    assert count == expected