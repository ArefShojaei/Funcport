import pytest
from funcport import list as funcport_list
from typing import Any

@pytest.mark.parametrize("hystack, expected", [
    ([1,2,3,4], 1),
    (["A", "B", "C"], "A"),
    ([True, False], True),
])
def test_get_first_list_item(hystack: list, expected: Any):
    value = funcport_list.current(hystack)

    assert value == expected
    assert type(value) == type(expected)