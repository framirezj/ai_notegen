from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de la base de datos, apuntando a una carpeta de datos dedicada y persistente
SQLALCHEMY_DATABASE_URL = "sqlite:///app/data/notes.db"

#Crea el motor de la base de datos usando la URL anterior. 
#El argumento check_same_thread=False permite que la base de datos SQLite sea usada por varios hilos (útil en aplicaciones web).
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#crea una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Crea una clase base para los modelos ORM. Todos los modelos de la base de datos deben heredar de esta clase.
base = declarative_base()

