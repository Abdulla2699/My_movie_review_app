from django.shortcuts import render

from rest_framework import generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
