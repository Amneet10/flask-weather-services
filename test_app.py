import unittest
from unittest.mock import patch
from app import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.requests.get')
    def test_temperature_valid_city(self, mocked_get):
        mocked_get.return_value.json.return_value = {'cod': 200, 'main': {'temp': 20}}
        response = self.app.post('/temperature', data={'city': 'London'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The temperature in London is 20°C', response.data)

    @patch('app.requests.get')
    def test_temperature_invalid_city(self, mocked_get):
        mocked_get.return_value.json.return_value = {'cod': '404', 'message': 'city not found'}
        response = self.app.post('/temperature', data={'city': 'NonexistentCity'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'City not found', response.data)

if __name__ == '__main__':
    unittest.main()
