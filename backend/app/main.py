#importamos fastapi
from fastapi import FastAPI
from . import models, database
from .routes import notes

#Esta línea crea automáticamente las tablas en la base de datos (si no existen) 
# usando la definición de tus modelos. Es útil para desarrollo y pruebas rápidas.
models.base.metadata.create_all(bind=database.engine)

app = FastAPI()

#le pasamos el router quien tiene las rutas
app.include_router(notes.router)

"""
@app.get("/")
def read_root():
    return {"message": "Hello World"}
"""
