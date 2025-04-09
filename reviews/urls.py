from django.urls import path
from .views import MovieListCreateView, ReviewListCreateView, ReviewListByMovieView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),  # CRUD for movies
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),  # CRUD for reviews
    path('movies/<int:movie_id>/reviews/', ReviewListByMovieView.as_view(), name='reviews-by-movie'),  # Filter reviews by movie
]
from .views import ReviewDetailView

urlpatterns = [
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
