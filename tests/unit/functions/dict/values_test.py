import pytest
from funcport import dict as funcport_dict

@pytest.mark.parametrize("map, expected", [
    (
        {
            "id" : 1,
            "name" : "Aref"
        },
        [1, "Aref"]
    ),
    ({}, [])
])
def test_get_dict_values(map: dict, expected: list):
    values = funcport_dict.values(map)

    assert type(values) == type(expected)
    assert values == expected