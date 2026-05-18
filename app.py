import os
import requests

API_URL = os.getenv("API_URL")

def obtener_datos(pais):
    url = f"{API_URL}/countries/{pais.lower()}" if pais.lower() != "global" else f"{API_URL}/all"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión.")
        return None
    except requests.exceptions.Timeout:
        print("❌ Timeout: el servidor demoró demasiado.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error general: {e}")
        return None

if __name__ == "__main__":
    pais = "chile"
    datos = obtener_datos(pais)
    if datos:
        print("\n===== DATOS COVID =====")
        print(f"País: {datos.get('country', 'Global')}")
        print(f"Casos Totales: {datos.get('cases')}")
        print(f"Casos Hoy: {datos.get('todayCases')}")
        print(f"Fallecidos: {datos.get('deaths')}")
        print(f"Recuperados: {datos.get('recovered')}")
