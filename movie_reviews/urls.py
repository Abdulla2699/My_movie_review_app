from django.contrib import admin
from django.urls import include, path
from reviews.views import ReviewListByMovieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reviews.urls')),  # Includes URLs from the reviews app
    path('api/movies/<int:movie_id>/reviews/', ReviewListByMovieView.as_view(), name='reviews-by-movie'),  # Filter reviews by movie
    path('api/token/', include('rest_framework_simplejwt.urls')),  # Authentication endpoints
]
