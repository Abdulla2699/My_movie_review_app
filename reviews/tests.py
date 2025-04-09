from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class MovieTests(APITestCase):
    def setUp(self):
        # Create a user for testing (replace with actual user details)
        self.username = 'tester'
        self.password = 'dalla010111'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        # Obtain a token by sending the username and password
        response = self.client.post(
            '/api/token/', 
            {'username': self.username, 'password': self.password}, 
            format='json'
        )
        self.token = response.data['access']  # Extract the access token

    def test_create_movie(self):
        url = reverse('movie-list')  # The URL for creating a movie
        data = {
            "title": "The Matrix",
            "description": "Sci-fi classic",
            "release_date": "1999-03-31"
        }

        # Include the token in the Authorization header
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Check that the status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
def test_get_movies(self):
    url = reverse('movie-list')  # URL for retrieving movies
    response = self.client.get(url, HTTP_AUTHORIZATION='Bearer ' + self.token)  # Include token in header
    
    # Check the status code (should return 200 OK) and that the response contains a list
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIsInstance(response.data, list)

