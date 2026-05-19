#!/bin/bash

# 1. Definimos la URL (por si acaso se necesita en el script)
API_URL="https://disease.sh/v3/covid-19"

echo "🚀 Iniciando Monitor COVID-19 CLI..."
echo "---------------------------------------"

# 2. Limpieza de contenedores previos
docker stop samplerunning 2>/dev/null
docker rm samplerunning 2>/dev/null

# 3. Construcción de la imagen
docker build -t app-covid .

# 4. Ejecución inyectando la URL directamente
echo "✅ Ejecución exitosa. Cargando interfaz..."
echo "---------------------------------------"
docker run -it --name samplerunning -e API_URL="https://disease.sh/v3/covid-19" app-covid
