import pytest

from utils import update_dict, clean_empty_keys


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (
            {"id": 1, "color": "black"},
            {"id": 2, "color": "red"},
            {"id": 2, "color": "red"},
        ),
        (
            {"id": 1, "color": "black"},
            {"id": 2, "color": "black"},
            {"id": 2, "color": "black"},
        ),
        (
            {"id": 1, "color": "black"},
            {"id": 2, "color": None},
            {"id": 2, "color": "black"},
        ),
        (
            {"id": 1, "color": "black"},
            {"id": None, "color": None},
            {"id": 1, "color": "black"},
        ),
    ],
    ids=["all keys change", "one key change", "one key None", "both keys None"],
)
def test_update_dict(a, b, expected):
    update_dict(a, b)
    assert a == expected


@pytest.mark.parametrize(
    "a, expected", [({"a": "1", "b": None, "c": "3", "d": None}, {"a": "1", "c": "3"})]
)
def test_clean_empty_keys(a, expected):
    assert expected == clean_empty_keys(a)
