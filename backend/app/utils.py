# Importa la clase CryptContext de la librería passlib, que es el motor principal para el hashing de contraseñas.
from passlib.context import CryptContext

# Crea una instancia de CryptContext. Esta es la configuración central para el manejo de contraseñas.
# - schemes=["bcrypt"]: Especifica que bcrypt será el algoritmo de hashing por defecto y preferido.
#   Bcrypt es una elección robusta y estándar en la industria para el hashing de contraseñas.

# - deprecated="auto": Le dice a passlib que si en el futuro se encuentra con un hash de un algoritmo
#   más antiguo (si lo añadieras a la lista de esquemas), lo actualice automáticamente al nuevo
#   esquema (bcrypt) la próxima vez que el usuario inicie sesión.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#REGISTER
# Define una función para hashear una contraseña.
# Recibe una contraseña en texto plano (string) y devuelve su versión hasheada (otro string).
def hash_password(password: str) -> str:
    # Utiliza el método .hash() del contexto que creamos para generar el hash de la contraseña.
    return pwd_context.hash(password)


#LOGIN
# Define una función para verificar si una contraseña en texto plano coincide con una contraseña ya hasheada.
# Devuelve True si coinciden, y False si no.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Utiliza el método .verify() del contexto. Este método es seguro contra ataques de temporización (timing attacks).
    # Compara el texto plano con el hash para ver si son la misma contraseña.
    return pwd_context.verify(plain_password, hashed_password)
