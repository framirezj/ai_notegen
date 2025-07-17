# AI NoteGen

Una aplicación web para generar, guardar y gestionar notas potenciadas por Inteligencia Artificial.

## Descripción General

Este proyecto consiste en una aplicación full-stack:

*   **Frontend:** Una aplicación de una sola página (SPA) construida con Vite + React, servida con Nginx para producción.
*   **Backend:** Una API RESTful construida en Python (por ejemplo, con FastAPI o Flask) que se encarga de la lógica de negocio y la comunicación con el modelo de IA. *(Nota: los detalles del backend son una suposición)*.

Ambos servicios están contenedorizados con Docker para facilitar el desarrollo y el despliegue.

## Requisitos Previos

*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/)

## Estructura del Proyecto (Sugerida)

```
/
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── Dockerfile.prod
│   ├── nginx/
│   │   └── nginx.conf
│   └── package.json
├── docker-compose.yml
├── .env.example
└── README.md
```

## Configuración y Ejecución

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO_DEL_PROYECTO>
```

### 2. Configurar Variables de Entorno

El frontend necesita saber la URL del backend para hacer las peticiones a la API. Esta configuración se gestiona a través de variables de entorno.

Crea un archivo `.env` en la raíz del proyecto, basándote en un posible archivo de ejemplo `.env.example`:

```bash
cp .env.example .env
```

Abre el archivo `.env` y ajusta los valores. El más importante para el frontend es `VITE_API_URL`.

**`.env`**
```env
# URL donde la API del backend estará accesible desde el navegador del usuario.
# En un entorno de producción, esto será tu dominio público.
# Para desarrollo local con docker-compose, a menudo es localhost en un puerto específico.
VITE_API_URL=http://localhost:8000/api
```

### 3. Levantar los Contenedores con Docker Compose

Una vez configurado el archivo `.env`, puedes construir y ejecutar toda la aplicación con un solo comando. Docker Compose leerá el archivo `.env` automáticamente y pasará las variables a los contenedores correspondientes.

```bash
docker-compose up --build -d
```

*   `--build`: Fuerza la reconstrucción de las imágenes si ha habido cambios en los `Dockerfile` o en el código fuente.
*   `-d`: Ejecuta los contenedores en segundo plano (detached mode).

La aplicación debería estar disponible en las siguientes URLs (pueden variar según tu `docker-compose.yml`):

*   **Frontend:** http://localhost:8080
*   **Backend API:** http://localhost:8000

### 4. Detener la Aplicación

Para detener todos los servicios, ejecuta:

```bash
docker-compose down
```

## Despliegue en Producción

El archivo `frontend/Dockerfile.prod` que has creado está perfectamente optimizado para producción. Utiliza una construcción en múltiples etapas (`multi-stage build`) para crear un contenedor Nginx ligero que solo contiene los archivos estáticos compilados del frontend.

El comando `docker-compose up --build` usará este Dockerfile para construir la imagen de producción. Es crucial que tu `docker-compose.yml` esté configurado para pasar el `VITE_API_URL` como un argumento de construcción (`build arg`), tal como se define en el `Dockerfile.prod`.

**Ejemplo de `docker-compose.yml` para el servicio frontend:**

```yaml
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.prod
      args:
        # Pasa la variable del .env como argumento de construcción
        - VITE_API_URL=${VITE_API_URL}
    ports:
      - "80:80"
# ... otros servicios como el backend
```