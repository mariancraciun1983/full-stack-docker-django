from rest_framework import serializers
from ..models import Genre


class GenresListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']
