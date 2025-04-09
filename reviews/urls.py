from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet
from .views import (
    MovieListCreateView,
    ReviewListCreateView,
    ReviewListByMovieView,
    ReviewDetailView
)
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),  # CRUD for movies
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),  # CRUD for reviews
    path('movies/<int:movie_id>/reviews/', ReviewListByMovieView.as_view(), name='reviews-by-movie'),  # Filter reviews by movie
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),  # Detail view for a review
    path('api/', include(router.urls)),
]
