from test import add_folder
import unittest
import requests

false_token = ''
true_token = ' '

class TestSomething(unittest.TestCase):

    def test_add_folder(self):
        self.assertEqual((add_folder(false_token, 'new-folder')).status_code, 401)
        response = add_folder(true_token, 'new-folder')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['href'], 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F' + 'new-folder')
        resp = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources",
            params={"path": 'new-folder'},
            headers={"Authorization": f"OAuth {true_token}"}
        )
        status = resp.status_code
        self.assertEqual(status, 200)
        self.assertEqual((add_folder(true_token, 'new-folder')).status_code, 409)