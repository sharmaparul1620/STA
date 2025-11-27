from app.calculator import add
from app.UserAuth import login


def test_integration_flow():
    # login first
    assert login("admin", "secret") is True

    # then perform some protected operation
    result = add(10, 5)
    assert result == 15
