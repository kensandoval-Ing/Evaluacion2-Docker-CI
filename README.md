# Monitor API COVID-19 CLI (Epidemiology Tool)

## 1. Definición del Contexto y Narrativa

* **Stakeholder:** Médico Jefe de Urgencias / Epidemiólogo de Hospital.
* **Propuesta de Valor (Problema/Solución):** En un entorno hospitalario de alta presión, el personal médico necesita datos epidemiológicos críticos para anticipar el flujo de pacientes internacionales y gestionar insumos médicos. Esta herramienta permite consultar, en segundos y desde la terminal, estadísticas actualizadas de COVID-19 (casos totales, fallecidos y recuperados), eliminando la dependencia de plataformas web lentas o saturadas en momentos de emergencia.

---

## 2. Guía de Configuración

Para garantizar la **Seguridad Técnica** y evitar la exposición de credenciales, el script utiliza variables de entorno mediante la librería \`os\`.

### Variables de Entorno Necesarias:
| Variable | Descripción | Ejemplo (Bash) |
| :--- | :--- | :--- |
| \`API_URL\` | URL base para la consulta de datos. | \`export API_URL="https://disease.sh/v3/covid-19"\`  |

> **Nota:** El archivo \`.gitignore\` está configurado para proteger archivos sensibles.

---

## 3. Instrucciones de Ejecución (Docker)

Esta solución está contenerizada para asegurar su funcionamiento en cualquier entorno técnico.
### A. Automatización con Script
El archivo \`build.sh\` genera el Dockerfile, construye la imagen y ejecuta el contenedor:
\`\`\`bash
chmod +x build.sh
./build.sh
\`\`\`

### B. Ejecución Manual
1. **Build:** \`docker build -t app-covid .\`
2. **Run:** \`docker run --name samplerunning -e API_URL=\$API_URL app-covid\` 

---

## 4. Estructura del Repositorio

La organización del proyecto sigue el estándar solicitado para una solución profesional:

Evaluacion2-Docker-CI/
├── app.py                    # Script principal de consulta API
├── build.sh                  # Script de automatización (Dockerfile, build y run)
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Archivos excluidos de Git
├── README.md                 # Documentación técnica
└── evidencias/
    ├── docker/
    │   ├── output.txt              # Registro de ejecución y logs reales
    │   └── screenshot.png          # Captura de salida en consola
    └── jenkins/
        ├── stage_view.png               # Visualización del Pipeline
        ├── console_output_build.png     # Logs de construcción en Jenkins
        ├── credentials.png              # Configuración de token GitHub
        └── pipeline_script.txt          # Código fuente del Pipeline
