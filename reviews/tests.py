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
def test_create_review(self):
    # First, create a movie to attach the review to
    movie = Movie.objects.create(
        title="The Matrix", description="Sci-fi classic", release_date="1999-03-31"
    )
    
    # URL for adding reviews to a specific movie
    url = reverse('reviews-by-movie', kwargs={'movie_id': movie.id})
    
    # Data for the review
    data = {
        "review": "Amazing movie!",
        "rating": 5
    }
    
    response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.token)
    
    # Check that the status code is 201 Created
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['review'], data['review'])
    self.assertEqual(response.data['rating'], data['rating'])
def test_get_reviews_by_movie(self):
    # First, create a movie and a review for that movie
    movie = Movie.objects.create(
        title="The Matrix", description="Sci-fi classic", release_date="1999-03-31"
    )
    
    Review.objects.create(
        movie=movie, review="Amazing movie!", rating=5
    )
    
    url = reverse('reviews-by-movie', kwargs={'movie_id': movie.id})
    response = self.client.get(url, HTTP_AUTHORIZATION='Bearer ' + self.token)
    
    # Check that the status code is 200 OK and reviews are returned
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['review'], "Amazing movie!")
    self.assertEqual(response.data[0]['rating'], 5)

