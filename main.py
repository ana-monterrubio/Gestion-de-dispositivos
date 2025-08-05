import requests
import json

BASE_URL = "https://reqres.in/api/users"

def manejar_respuesta(r):
    if r.status_code in [200, 201]:
        print("Operación exitosa.")
    elif r.status_code == 400:
        print("Error 400: Solicitud incorrecta.")
    elif r.status_code == 401:
        print("Error 401: No autorizado. Falta API Key.")
    elif r.status_code == 404:
        print("Error 404: Recurso no encontrado.")
    elif r.status_code == 500:
        print("Error 500: Error interno del servidor.")
    else:
        print(f"Código inesperado: {r.status_code}")

# 1. Agregar dispositivo (POST)
def agregar_dispositivo(nombre, trabajo):
    payload = {"name": nombre, "job": trabajo}
    r = requests.post(BASE_URL, json=payload)
    print("\n[POST] Agregar dispositivo:")
    print("Código de estado:", r.status_code)
    manejar_respuesta(r)
    print("Respuesta JSON:", json.dumps(r.json(), indent=4))

# 2. Listar dispositivos (GET)
def listar_dispositivos():
    r = requests.get(BASE_URL)
    print("\n[GET] Listar dispositivos:")
    print("Código de estado:", r.status_code)
    manejar_respuesta(r)
    print("Respuesta JSON:", json.dumps(r.json(), indent=4))

# 3. Actualizar dispositivo (PUT)
def actualizar_dispositivo(id_dispositivo, nombre, trabajo):
    payload = {"name": nombre, "job": trabajo}
    r = requests.put(f"{BASE_URL}/{id_dispositivo}", json=payload)
    print("\n[PUT] Actualizar dispositivo:")
    print("Código de estado:", r.status_code)
    manejar_respuesta(r)
    print("Respuesta JSON:", json.dumps(r.json(), indent=4))

# 4. Eliminar dispositivo (DELETE)
def eliminar_dispositivo(id_dispositivo):
    r = requests.delete(f"{BASE_URL}/{id_dispositivo}")
    print("\n[DELETE] Eliminar dispositivo:")
    print("Código de estado:", r.status_code)
    manejar_respuesta(r)
    if r.status_code == 204:
        print("Dispositivo eliminado correctamente.")

# ==========================
# Ejecución de funciones
# ==========================
if __name__ == "__main__":
    listar_dispositivos()
    agregar_dispositivo("Router Cisco", "Configuración")
    actualizar_dispositivo(2, "Switch Cisco", "Actualización firmware")
    eliminar_dispositivo(2)