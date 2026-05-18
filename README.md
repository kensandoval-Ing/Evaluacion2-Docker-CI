# Monitor API COVID-19 CLI

## 1. Definición del Contexto y Narrativa

* **Stakeholder:** Médico Jefe de Urgencias / Epidemiólogo de Hospital[cite: 13].
* **Propuesta de Valor (Problema/Solución):** En situaciones de alta demanda hospitalaria, un Médico Jefe necesita monitorear el estado epidemiológico global para gestionar la disponibilidad de camas críticas. Esta herramienta elimina la dependencia de tableros web lentos, permitiendo consultar datos clave (casos nuevos, activos y fallecidos) en segundos directamente desde la terminal[cite: 15].

---

## 2. Guía de Configuración

Para garantizar la **Seguridad Técnica** y evitar el *hardcoding* de credenciales, el script utiliza variables de entorno leídas mediante la librería \`os\` de Python[cite: 26, 27].

### Variables de Entorno Necesarias:
| Variable | Descripción | Ejemplo (Bash) |
| :--- | :--- | :--- |
| \`API_URL\` | URL base para la consulta de datos. | \`export API_URL="https://disease.sh/v3/covid-19"\` [cite: 22] |

> **Nota:** Se ha incluido un archivo \`.gitignore\` para evitar la subida accidental de archivos sensibles o entornos virtuales.

---

## 3. Instrucciones de Ejecución (Docker)

Este proyecto utiliza una arquitectura de contenedores para asegurar la reproducibilidad del entorno[cite: 30].

### A. Ejecución mediante Script de Automatización
El archivo \`build.sh\` genera el Dockerfile, construye la imagen y ejecuta el contenedor automáticamente[cite: 31]:
\`\`\`bash
chmod +x build.sh
./build.sh
\`\`\`

### B. Comandos Manuales de Docker
Si prefiere realizar el despliegue de forma manual[cite: 23]:

1. **Construir la imagen:**
   \`\`\`bash
   docker build -t app-covid .
   \`\`\`
2. **Ejecutar el contenedor:**
   \`\`\`bash
   docker run --name samplerunning -e API_URL=\$API_URL app-covid
   \`\`\`

---

## 4. Estructura del Repositorio [cite: 75]

* \`app.py\`: Script principal (procesa $\ge3$ campos y maneja $\ge4$ tipos de errores)[cite: 25].
* \`build.sh\`: Script de automatización de infraestructura[cite: 79].
* \`output.txt\`: Registro de salida de \`docker ps -a\` y logs de la API[cite: 33].
* \`evidencias/jenkins/\`: Capturas obligatorias del flujo CI/CD[cite: 43].
