#importamos fastapi
from fastapi import FastAPI
from . import models, database
from .routes import notes
from fastapi.middleware.cors import CORSMiddleware

#Esta línea crea automáticamente las tablas en la base de datos (si no existen) 
# usando la definición de tus modelos. Es útil para desarrollo y pruebas rápidas.
models.base.metadata.create_all(bind=database.engine)

app = FastAPI()


# 👇 Aquí configuramos CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # o ["*"] para permitir todo (menos seguro)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#le pasamos el router quien tiene las rutas
app.include_router(notes.router)

"""
@app.get("/")
def read_root():
    return {"message": "Hello World"}
"""
