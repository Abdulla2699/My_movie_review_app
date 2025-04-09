from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie

class MovieTests(APITestCase):
    def test_create_movie(self):
        data = {"title": "Test Movie", "description": "Just a test.", "release_date": "2025-01-01"}
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

