import pytest
from funcport import dict as funcport_dict

@pytest.mark.parametrize("map, expected", [
    (
        {
            "id" : 1,
            "name" : "Aref"
        },
        ["id", "name"]
    ),
    ({}, [])
])
def test_get_dict_keys(map: dict, expected: list):
    keys = funcport_dict.keys(map)

    assert type(keys) == type(expected)
    assert keys == expected