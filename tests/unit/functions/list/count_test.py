import pytest
from funcport import list


@pytest.mark.parametrize("data, expected", [
    ([1,2,3], 3),
    (["Hello", "world"], 2),
    (["a"], 1)
])
def test_get_list_size(data: list, expected: int):
    value = list.count(data)

    assert value == expected
    assert type(value) == type(expected)