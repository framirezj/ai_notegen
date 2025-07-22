from app.auth import create_access_token, get_current_user
from fastapi import HTTPException
import pytest
from jose import jwt
from datetime import datetime, timedelta, timezone


class User:
    def __init__(self, email):
        self.email = email


#Genera Token
def test_create_access_token():    

    #datos de entrada
    user = User("fran@example.com")

    data={"sub": user.email}
    expires = timedelta(minutes=15)

    #generar token
    token = create_access_token(data, expires)

    #assert 1
    assert token is not None
    assert isinstance(token, str)

#Comprueba token valido
def test_get_current_user():

    user = User("test@example.com")
    token = create_access_token(data={"sub": user.email})

    #la function retorna el username que es el email del usuario.
    email_username = get_current_user(token)

    assert user.email == email_username

#Comprueba token expirado
def test_get_current_user_raises_exception_on_expired_token():

    email = "test@example.com"
    data = {"sub": email}
    expires_delta = timedelta(minutes=-30)

    token = create_access_token(data, expires_delta)

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token)

    assert exc_info.value.status_code == 401


#Comprueba una firma invalida
def test_get_current_user_raises_exception_on_invalid_signature():

    payload = {
        "sub": "test@example.com",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }

    invalid_token = jwt.encode(
        payload,
        "SECRET_INCORRECT",
        algorithm="HS256"
        )
    
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token=invalid_token)

    assert exc_info.value.status_code == 401



