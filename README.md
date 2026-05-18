# Monitor API COVID-19 CLI

## 1. Contexto y Narrativa
* **Stakeholder:** Médico Jefe de Urgencias / Epidemiólogo del Hospital.
* **Propuesta de Valor (Problema/Solución):** Un Médico Jefe necesita monitorear rápidamente el estado epidemiológico (casos nuevos, activos y fallecidos) de diferentes países. Esta herramienta le permite acceder a datos actualizados en segundos sin depender de plataformas lentas, ayudándole a anticipar posibles olas de contagio por pacientes internacionales y a gestionar de forma eficiente los insumos y camas del hospital[cite: 13, 14, 15].

## 2. Guía de Configuración
Este proyecto utiliza variables de entorno para proteger la ruta de la API. Antes de ejecutar, debes configurar la siguiente variable[cite: 22]:
* API_URL: URL base de la API (ej. https://disease.sh/v3/covid-19)

## 3. Instrucciones de Ejecución (Docker)
Para construir la imagen y ejecutar el contenedor, utiliza el script de automatización[cite: 23]:
./build.sh
