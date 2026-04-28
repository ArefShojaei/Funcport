import pytest
from funcport import list as funcport_list

@pytest.mark.parametrize("hystack, value, expected", [
    ([1,2,3], "*", ["*","*","*"]),
    (["A", "B", "C"], "*", ["*","*","*"]),
    ([True, False, True], "*", ["*","*","*"]),
    (["Welcome", "back", "man!"], "#", ["#","#","#"]),
])
def test_fill_list_with_value(hystack: list, value: str, expected: list):
    filled_list = funcport_list.fill(hystack, value)

    assert filled_list == expected
    assert len(filled_list) == len(expected)
    assert type(filled_list) == type(expected)
    assert value in filled_list