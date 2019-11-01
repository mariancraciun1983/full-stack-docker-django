from rest_framework import serializers
from ..models import Movie
from app_genres.models import Genre


# class MoviesGenreListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ['slug']

class MoviesGenreListSerializer(serializers.StringRelatedField):
    def to_representation(self, genre):
        return genre.slug

class MoviesListSerializer(serializers.HyperlinkedModelSerializer):
    genres = MoviesGenreListSerializer(source='genre', many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'slug', 'genres', 'description', 'image', 'price']
