



echo "Construyendo imagen Docker..."
docker build -t app-covid .
echo "Ejecutando contenedor..."
docker run --name samplerunning --env API_URL="https://disease.sh/v3/covid-19" app-covid
