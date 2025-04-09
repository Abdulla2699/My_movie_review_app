from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # View for anyone, create requires authentication

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # View for anyone, create requires authentication

class ReviewListByMovieView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)
    permission_classes = [IsAuthenticatedOrReadOnly]  # Filter reviews by movie ID

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Only authenticated
from django_filters.rest_framework import DjangoFilterBackend

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'release_date']
