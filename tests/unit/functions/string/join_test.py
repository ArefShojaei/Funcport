import pytest
from funcport import string


@pytest.mark.parametrize("wordList, separator, expected", [
    (["a", "b", "c"], "*", "a*b*c"),
    (["Hello", "world"], " ", "Hello world")
])
def test_join_list_of_string_to_string(wordList: list, separator: str, expected: str):
    value = string.join(separator, wordList)

    assert value == expected