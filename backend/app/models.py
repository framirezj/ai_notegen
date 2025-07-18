
#importamos las clases necesarias
from sqlalchemy import Column, Integer, String
from .database import base

#definie la clase Note y en su argumento hereda la clase base que importamos
class Note(base):

    #representa el nombre de la tabla que estara en la base de datos con sus respectivas propiedades
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)


#modelo para usuario
class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)