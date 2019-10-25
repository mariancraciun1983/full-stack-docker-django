from rest_framework import viewsets
from ..models import Movie
from .serializers import MoviesListSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = None
    serializer_class = MoviesListSerializer
