# Monitor API COVID-19 CLI (Epidemiology Tool)

## 1. Definición del Contexto y Narrativa

* **Stakeholder:** Médico Jefe de Urgencias / Epidemiólogo de Hospital[cite: 13].
* **Propuesta de Valor (Problema/Solución):** En un entorno hospitalario de alta presión, el personal médico necesita datos epidemiológicos críticos para anticipar el flujo de pacientes internacionales y gestionar insumos médicos. Esta herramienta permite consultar, en segundos y desde la terminal, estadísticas actualizadas de COVID-19 (casos totales, fallecidos y recuperados), eliminando la dependencia de plataformas web lentas o saturadas en momentos de emergencia[cite: 15].

---

## 2. Guía de Configuración

Para garantizar la **Seguridad Técnica** y evitar la exposición de credenciales, el script utiliza variables de entorno mediante la librería \`os\`[cite: 26, 27].

### Variables de Entorno Necesarias:
| Variable | Descripción | Ejemplo (Bash) |
| :--- | :--- | :--- |
| \`API_URL\` | URL base para la consulta de datos. | \`export API_URL="https://disease.sh/v3/covid-19"\` [cite: 22] |

> **Nota:** El archivo \`.gitignore\` está configurado para proteger archivos sensibles[cite: 29].

---

## 3. Instrucciones de Ejecución (Docker)

Esta solución está contenerizada para asegurar su funcionamiento en cualquier entorno técnico[cite: 30].

### A. Automatización con Script
El archivo \`build.sh\` genera el Dockerfile, construye la imagen y ejecuta el contenedor[cite: 31]:
\`\`\`bash
chmod +x build.sh
./build.sh
\`\`\`

### B. Ejecución Manual
1. **Build:** \`docker build -t app-covid .\` [cite: 23]
2. **Run:** \`docker run --name samplerunning -e API_URL=\$API_URL app-covid\` [cite: 23]

---

## 4. Estructura del Repositorio

La organización del proyecto sigue el estándar solicitado para una solución profesional[cite: 75]:

sample-app/
│
├── app.py              # Script principal que consulta la API [cite: 78, 84]
├── build.sh            # Script de automatización (Dockerfile, build y run) [cite: 79, 85]
├── requirements.txt    # Dependencias Python [cite: 77, 85]
├── .gitignore          # Archivos excluidos del repositorio [cite: 80]
├── README.md           # Documentación del proyecto [cite: 81]
└── evidencias/         # Carpeta de respaldos [cite: 82]
    ├── docker/         # Resultados de la contenerización [cite: 83]
    │   ├── output.txt        # docker ps -a + logs con datos reales [cite: 86, 87]
    │   └── screenshot.png    # Captura de la salida en consola [cite: 88]
    └── jenkins/        # Evidencias de CI/CD [cite: 89]
        ├── stage_view.png            # Visualización de etapas [cite: 90]
        ├── console_output_build.png  # Logs de construcción [cite: 91]
        ├── credentials.png           # Configuración segura de token [cite: 92]
        └── pipeline_script.txt       # Código del pipeline orquestado [cite: 93]
