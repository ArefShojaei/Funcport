import pytest
from funcport import string


@pytest.mark.parametrize("text, keyboard, expected", [
    ("Software Engineer", "Engineer", True),
    ("Software Engineer", "engineer", False),
    ("Software Engineer", "Developer", False),
    ("Software developer", "developer", True)
])
def test_search_keyboard_in_string(text: str, keyboard: str, expected: bool):
    isExists = string.contains(text, keyboard)

    assert isExists == expected