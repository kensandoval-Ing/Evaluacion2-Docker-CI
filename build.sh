#!/bin/bash
echo "Construyendo imagen Docker..."
docker build --network host -t app-covid .

echo "Ejecutando contenedor..."
docker run --name samplerunning --env API_URL="https://disease.sh/v3/covid-19" app-covid
