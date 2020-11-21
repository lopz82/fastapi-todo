from crypto import hash_password, is_correct_password


def test_hash_password():
    passwd = "test"
    hashed = hash_password(passwd)
    assert is_correct_password(passwd, hashed)
