#importamos fastapi
from fastapi import FastAPI, status
from . import models, database
from .routes import notes
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

FRONTEND_URL = os.getenv("FRONTEND_URL")

if not FRONTEND_URL:
    raise ValueError("FRONTEND_URL no está definida en el archivo .env")


#Esta línea crea automáticamente las tablas en la base de datos (si no existen) 
# usando la definición de tus modelos. Es útil para desarrollo y pruebas rápidas.
models.base.metadata.create_all(bind=database.engine)

app = FastAPI()


# 👇 Aquí configuramos CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],  # o ["*"] para permitir todo (menos seguro)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=status.HTTP_200_OK, tags=['Health Check'])
def health_check():
    return {"status": "ok"}

#le pasamos el router quien tiene las rutas
app.include_router(notes.router)


