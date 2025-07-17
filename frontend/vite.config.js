import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [tailwindcss(), react()],
  server: {
    // Escucha en '0.0.0.0' para ser accesible desde fuera del contenedor.
    // Esto es CRUCIAL para Docker.
    host: '0.0.0.0', 
    
    // Asegúrate de que el puerto sea el mismo que expusiste en docker-compose.
    port: 5173,

    // Esta sección ayuda a que el Hot Module Replacement (HMR) funcione.
    watch: {
      // Usa "polling" para detectar cambios en los archivos.
      // Es más intensivo para la CPU, pero es la forma más fiable
      // de detectar cambios a través de un volumen de Docker.
      usePolling: true,
    }
  }
})
