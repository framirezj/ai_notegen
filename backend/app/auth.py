# Importa las clases 'datetime' y 'timedelta' para manejar fechas y duraciones, necesarias para la expiración del token.
from datetime import datetime, timedelta, timezone
# Importa 'JWTError' para manejar posibles errores y 'jwt' para crear y firmar los JSON Web Tokens.
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from .database import get_db

from .models import User


# Carga las variables de entorno del archivo .env
load_dotenv()

# Define la clave secreta utilizada para firmar digitalmente el token. Es crucial para la seguridad.
# Lee la clave secreta desde las variables de entorno. NUNCA la dejes escrita en el código.
SECRET_KEY = os.getenv("SECRET_KEY", "test_clave")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definida en el archivo .env")

# Especifica el algoritmo de encriptación que se usará para la firma. HS256 es un estándar común.
ALGORITHM = "HS256"
# Establece el tiempo de vida por defecto de un token de acceso en minutos.
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define la función que creará el token de acceso. Recibe datos (payload) y una duración opcional.
def create_access_token(data: dict, expires_delta: timedelta = None):
    # Crea una copia del diccionario de datos para no modificar el original.
    to_encode = data.copy()
    # Calcula la fecha y hora de expiración en UTC. Usa la duración proporcionada o la de por defecto (30 minutos).
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # Añade la fecha de expiración al diccionario que se codificará. 'exp' es un campo estándar de JWT.
    to_encode.update({"exp": expire})
    # Codifica el diccionario en un token JWT, firmándolo con la clave secreta y el algoritmo.
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # o el path que uses


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == username).first()
    if user is None:
        raise credentials_exception
    
    return user