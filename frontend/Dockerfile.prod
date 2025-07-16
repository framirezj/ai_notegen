# frontend/Dockerfile

# --- Etapa de Construcción (Builder) ---
FROM node:18 as builder
WORKDIR /app

# Copiar archivos de dependencias y instalar
COPY package.json package-lock.json ./
RUN npm install

# Copiar el resto del código fuente
COPY . .

# Construir la aplicación
RUN npm run build

# --- Etapa de Producción (Final) ---
FROM node:18-alpine
WORKDIR /app
RUN npm install -g serve

# Copiar solo los artefactos de construcción de la etapa anterior
COPY --from=builder /app/dist ./dist

EXPOSE 5173
CMD ["serve", "-s", "dist", "-l", "5173"]
