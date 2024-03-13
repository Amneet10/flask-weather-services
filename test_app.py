import unittest
from unittest.mock import patch
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('app.requests.get')
    def test_temperature(self, mock_get):
        # Mock response from the OpenWeatherMap API
        mock_get.return_value.json.return_value = {
            'cod': 200,
            'main': {'temp': 20}
        }

        # Make a POST request to the /temperature endpoint
        response = self.client.post('/temperature', data={'city': 'London'})

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected temperature
        self.assertIn(b'The temperature in London is 20\xc2\xb0C', response.data)

    @patch('app.requests.get')
    def test_temperature_city_not_found(self, mock_get):
        # Mock response from the OpenWeatherMap API
        mock_get.return_value.json.return_value = {'cod': '404', 'message': 'city not found'}

        # Make a POST request to the /temperature endpoint
        response = self.client.post('/temperature', data={'city': 'UnknownCity'})

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the response contains 'City not found'
        self.assertIn(b'City not found', response.data)

if __name__ == '__main__':
    unittest.main()
