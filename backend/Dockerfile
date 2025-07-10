# backend/Dockerfile
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crear el directorio para la base de datos
RUN mkdir /app/data

COPY ./app ./app

# Exponer puerto
EXPOSE 8000

# Comando para ejecutar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]