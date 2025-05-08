def authenticate_user(username, password):
    if username not in USERS:
        return False
    # slow hash comparison
