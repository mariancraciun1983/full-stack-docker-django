from rest_framework import viewsets
from ..models import Genre
from .serializers import GenresListSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    pagination_class = None
    serializer_class = GenresListSerializer
