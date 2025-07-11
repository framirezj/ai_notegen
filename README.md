# 🧠 AI NoteGen (aun no agrego AI)

**AI NoteGen** es una aplicación web completa que te permite gestionar tus notas de forma sencilla y eficaz. Crea, edita, elimina y visualiza tus notas en una interfaz limpia e intuitiva.

## ✨ Características

- **Gestión de notas CRUD:** Crea, lee, actualiza y elimina notas.
- **Interfaz de usuario moderna:** Un diseño limpio y atractivo construido con React y estilizado con Tailwind CSS.
- **Backend robusto:** Un potente API RESTful construido con FastAPI y SQLAlchemy.
- **Contenerización:** Dockerizado para un despliegue y desarrollo sencillos.
- **Componentes reutilizables:** Código de frontend modular y fácil de mantener.

## 🚀 Tecnologías Utilizadas

### Backend
- **FastAPI:** Un moderno y rápido framework web de Python para construir APIs.
- **SQLAlchemy:** El kit de herramientas SQL de Python y el Mapeador Relacional de Objetos.
- **Pydantic:** Validación de datos y gestión de la configuración mediante anotaciones de tipo de Python.
- **Uvicorn:** Un servidor ASGI ultrarrápido.

### Frontend
- **React:** Una biblioteca de JavaScript para construir interfaces de usuario.
- **Vite:** Una herramienta de construcción de frontend que mejora significativamente la experiencia de desarrollo.
- **Axios:** Un cliente HTTP basado en promesas para el navegador y node.js.
- **Tailwind CSS:** Un framework de CSS de utilidad primero para un diseño rápido de UI.
- **Lucide React:** Un conjunto de iconos SVG simple y bonito.

### Despliegue
- **Docker & Docker Compose:** Para la contenerización y la gestión de aplicaciones multicontenedor.

## 🏁 Cómo Empezar

### Prerrequisitos

- Docker y Docker Compose instalados en tu máquina.

### Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/ai-notegen.git
   cd ai-notegen
   ```

2. **Inicia la aplicación con Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **¡Accede a la aplicación!**
   - El **frontend** estará disponible en `http://localhost:5173`.
   - El **backend** estará disponible en `http://localhost:8000/docs`.
