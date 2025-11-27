def login(username, password):
    if not username or not password:
        return False

    # pretend this is from database
    correct_user = "admin"
    correct_pass = "secret"

    return username == correct_user and password == correct_pass
