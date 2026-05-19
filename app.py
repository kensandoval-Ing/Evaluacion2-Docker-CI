import os
import requests

def consultar_covid():
    # Uso obligatorio de os.getenv para seguridad [cite: 27, 55]
    api_base_url = os.getenv('API_URL')
    
    if not api_base_url:
        print("Error: La variable de entorno API_URL no está configurada.")
        return

    pais = input("🏥 Ingrese el país a consultar (en inglés, ej: Chile, USA, Italy): ").strip()

    try:
        # Consulta dinámica a la API
        url = f"{api_base_url}/countries/{pais}"
        response = requests.get(url, timeout=10)
        
        # 1. Manejo de error 404 (País no encontrado) 
        response.raise_for_status() 
        
        data = response.json()

        # Procesamiento de >= 3 campos de datos [cite: 25, 48]
        print(f"\n✅ REPORTE EPIDEMIOLÓGICO: {data['country'].upper()}")
        print(f"-----------------------------------")
        print(f"📌 Casos Totales: {data['cases']}")
        print(f"📌 Casos de Hoy:  {data['todayCases']}")
        print(f"📌 Fallecidos:    {data['deaths']}")
        print(f"📌 Recuperados:   {data['recovered']}")
        print(f"📌 Casos Activos: {data['active']}")
        print(f"-----------------------------------")

    # Manejo robusto de >= 4 tipos de errores [cite: 25, 50]
    except requests.exceptions.HTTPError:
        print(f"❌ Error 404: No se encontró información para '{pais}'. Verifique el nombre.")
    except requests.exceptions.ConnectionError:
        print("❌ Error de Conexión: No se pudo establecer contacto con el servidor.")
    except requests.exceptions.Timeout:
        print("❌ Error de Tiempo: La API tardó demasiado en responder (Timeout).")
    except Exception as e:
        print(f"❌ Error Inesperado: {e}")

if __name__ == "__main__":
    consultar_covid()
