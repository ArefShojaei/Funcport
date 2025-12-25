import pytest
from funcport import list
from typing import Any


@pytest.mark.parametrize("input, expected", [
    ([1,2,3], 3),
    (["Hello", "world"], 2),
    (["a"], 1),
    ([], 0)
])
def test_get_list_size(input: list, expected: int):
    assert list.count(input) == expected
    assert type(list.count(input)) == type(expected)

@pytest.mark.parametrize("input", [
    None, 
    123, 
    45.67, 
    "text", 
    {"dict": 1}, 
    {"set"}, 
    b"bytes", 
    True, 
    False, 
    lambda x: x, 
    object()
])
def test_get_list_size_with_invalid_input(input: Any):
    with pytest.raises(TypeError) as error:
        list.count(input)

    assert str(error.value) == "input should be list!"