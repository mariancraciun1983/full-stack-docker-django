from rest_framework import serializers
from ..models import Movie


class MoviesListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'slug', 'genre', 'description', 'image', 'price']
