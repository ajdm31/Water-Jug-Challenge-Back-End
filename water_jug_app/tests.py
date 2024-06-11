from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class WaterJugAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_input(self):
        response = self.client.post('/waterjug/', {
            'x_capacity': 3,
            'y_capacity': 5,
            'z_amount_wanted': 4
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("solution", response.data)
        self.assertEqual(response.data["solution"][-1]["status"], "Solved")

    def test_invalid_input(self):
        response = self.client.post('/waterjug/', {
            'x_capacity': -3,
            'y_capacity': 5,
            'z_amount_wanted': 4
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
