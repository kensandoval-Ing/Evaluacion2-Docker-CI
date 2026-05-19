echo "Limpiando contenedores antiguos..."
docker stop samplerunning 2>/dev/null
docker rm samplerunning 2>/dev/null

echo "Construyendo imagen Docker..."
docker build -t app-covid .

echo "Ejecutando contenedor interactivo..."
# El flag -it es vital para que puedas escribir el país
docker run -it --name samplerunning -e API_URL=$API_URL app-covid
