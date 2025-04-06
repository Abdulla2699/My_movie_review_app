from rest_framework import viewsets, permissions
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer, UserSerializer
from django.contrib.auth.models import User

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]