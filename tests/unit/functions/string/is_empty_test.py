import pytest
from funcport import string

@pytest.mark.parametrize("text", [""])
def test_is_empty_string(text: str):
    is_empty = string.is_empty(text)

    assert is_empty == True
    assert type(is_empty) == bool