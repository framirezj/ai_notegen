from app.auth import create_access_token
from datetime import timedelta



class User:
    def __init__(self, email):
        self.email = email

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



