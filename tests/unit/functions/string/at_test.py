import pytest
from funcport import string


@pytest.mark.parametrize("text, index, expected", [
    ("Python", -1, "n"),
    ("Python", 0, "P"),
    ("Python", 1, "y"),
])
def test_get_correct_string_index(text: str, index: int, expected: str):
    value = string.at(text, index)

    assert value == expected

@pytest.mark.parametrize("text, index, expected", [
    ("Python", -1, "N"),
    ("Python", 0, "p"),
    ("Python", 1, "Y"),
])
def test_get_incorrect_string_index(text: str, index: int, expected: str):
    value = string.at(text, index)

    assert value != expected

@pytest.mark.parametrize("text, index", [
    ("Python", 10),
    ("Python", -10),
])
def test_throw_index_error_with_invalid_argument(text: str, index: int):
    with pytest.raises(IndexError, match="string index out of range"):
        string.at(text, index)

@pytest.mark.parametrize("text, index, expected_message", [
    # Text param
    (0, 0, "text should be string!"),
    (["list"], 0, "text should be string!"),
    (("tuple",), 0, "text should be string!"),
    ({"dict" : []}, 0, "text should be string!"),
    
    # Index param
    ("Python", ["list"], "index should be int!"),
    ("Python", ("tuple",), "index should be int!"),
    ("Python", {"dict" : []}, "index should be int!"),
])
def test_get_string_index_with_invalid_argument(text: str, index: int, expected_message: str):
    with pytest.raises(TypeError) as error:
        string.at(text, index)

    assert str(error.value) == expected_message