import pytest

from utils import update_dict


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
