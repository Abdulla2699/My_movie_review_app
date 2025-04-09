from django.urls import path
from .views import MovieListCreateView, ReviewListCreateView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]
