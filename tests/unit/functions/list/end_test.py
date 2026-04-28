import pytest
from funcport import list as funcport_list
from typing import Any

@pytest.mark.parametrize("hystack, expected", [
    ([1,2,3,4], 4),
    (["A", "B", "C"], "C"),
    ([True, False], False),
])
def test_get_last_list_item(hystack: list, expected: Any):
    value = funcport_list.end(hystack)

    assert value == expected
    assert type(value) == type(expected)