#importamos fastapi
from fastapi import FastAPI, status
from . import models, database
from .routes import notes
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

# Prioriza la variable de producción (lista de orígenes separados por coma)
# Si no existe, usa la variable de desarrollo (una sola URL) como fallback.
cors_origins_str = os.getenv("CORS_ORIGINS")
if cors_origins_str:
    origins = cors_origins_str.split(',')
else:
    origins = [os.getenv("FRONTEND_URL", "http://localhost:5173")]


#Esta línea crea automáticamente las tablas en la base de datos (si no existen) 
# usando la definición de tus modelos. Es útil para desarrollo y pruebas rápidas.
models.base.metadata.create_all(bind=database.engine)

app = FastAPI()


# 👇 Aquí configuramos CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=status.HTTP_200_OK, tags=['Health Check'])
def health_check():
    return {"status": "ok"}

#le pasamos el router quien tiene las rutas
app.include_router(notes.router)


