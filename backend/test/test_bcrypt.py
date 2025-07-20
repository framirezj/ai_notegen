from app.utils import hash_password, verify_password

def test_hash_password():
    password = "password_test"

    password_hashed = hash_password(password)

    assert password_hashed != password
    assert password_hashed.startswith("$2b$")


def test_verify_password():
    password = "password_test"
    password_hashed = hash_password(password)

    assert verify_password(password, password_hashed) is True
    assert verify_password("otra_password", password_hashed) is False
