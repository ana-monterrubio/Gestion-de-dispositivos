import requests
import unittest
import json

class NetworkDeviceManager:
    BASE_URL = "https://reqres.in/api/users"  # Usamos el endpoint de usuarios 
    
    def add_device(self, device_data):
        """Agrega un dispositivo (POST)"""
        try:
            response = requests.post(self.BASE_URL, json=device_data)
            if response.status_code in [200, 201]:
                return response.json()
            return {"error": response.json().get("error", "Unknown error"), "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": 500}

    def list_devices(self):
        """Lista dispositivos (GET)"""
        try:
            response = requests.get(self.BASE_URL)
            if response.status_code == 200:
                return response.json()
            return {"error": response.json().get("error", "Unknown error"), "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": 500}

    def update_device(self, device_id, update_data):
        """Actualiza un dispositivo (PUT)"""
        try:
            response = requests.put(f"{self.BASE_URL}/{device_id}", json=update_data)
            if response.status_code == 200:
                return response.json()
            return {"error": response.json().get("error", "Unknown error"), "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": 500}

    def delete_device(self, device_id):
        """Elimina un dispositivo (DELETE)"""
        try:
            response = requests.delete(f"{self.BASE_URL}/{device_id}")
            if response.status_code == 204:
                return {"status": "success", "message": "Device deleted"}
            return {"error": response.json().get("error", "Unknown error"), "status_code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": 500}


class TestNetworkDeviceManager(unittest.TestCase):
    def setUp(self):
        self.manager = NetworkDeviceManager()
        self.test_device = {
            "name": "Cisco_Router_01",
            "job": "Network Device"  # reqres.in espera 'name' y 'job'
        }

    def test_add_device(self):
        result = self.manager.add_device(self.test_device)
        self.assertIn("id", result)  # reqres.in devuelve 'id' al crear usuario

    def test_list_devices(self):
        result = self.manager.list_devices()
        self.assertIn("data", result)  # reqres.in devuelve 'data' con la lista

    def test_update_device(self):
        update_data = {"job": "Updated Device"}
        result = self.manager.update_device(2, update_data)
        self.assertIn("job", result)  # Verificamos que se actualizó el campo

    def test_delete_device(self):
        result = self.manager.delete_device(2)
        self.assertEqual(result["status_code"], 204)  # reqres.in devuelve 204 al borrar

    def test_error_handling(self):
        # Test con ID que no existe (debería dar 404)
        result = self.manager.update_device(999, {})
        self.assertEqual(result["status_code"], 404)


if __name__ == "__main__":
    unittest.main()