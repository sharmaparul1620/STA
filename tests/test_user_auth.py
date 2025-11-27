from app.UserAuth import login

def test_login_success():
    assert login("admin", "secret") is True

def test_login_failure():
    assert login("wrong", "pass") is False

def test_empty_credentials():
    assert login("", "") is False
