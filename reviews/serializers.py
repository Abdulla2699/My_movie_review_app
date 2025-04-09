from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() 
    class Meta:
        model = Review
        fields = ['movie', 'user', 'rating', 'comment']