import unittest
import requests

BASE_URL = "https://reqres.in/api/users"

class TestAPIDispositivos(unittest.TestCase):

    def test_get_dispositivos(self):
        r = requests.get(BASE_URL)
        self.assertEqual(r.status_code, 200, "GET debería devolver 200")

    def test_post_dispositivo(self):
        payload = {"name": "Router Cisco", "job": "Configuración"}
        r = requests.post(BASE_URL, json=payload)
        self.assertIn(r.status_code, [201, 401], "POST debería devolver 201 o 401")

    def test_put_dispositivo(self):
        payload = {"name": "Switch Cisco", "job": "Actualización firmware"}
        r = requests.put(f"{BASE_URL}/2", json=payload)
        self.assertIn(r.status_code, [200, 401], "PUT debería devolver 200 o 401")

    def test_delete_dispositivo(self):
        r = requests.delete(f"{BASE_URL}/2")
        self.assertIn(r.status_code, [204, 401], "DELETE debería devolver 204 o 401")

if __name__ == "__main__":
    unittest.main()