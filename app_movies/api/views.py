from rest_framework import viewsets
from ..models import Movie
from .serializers import MoviesListSerializer
from rest_framework.permissions import AllowAny


class ListViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    permission_classes = (AllowAny,)
    queryset = Movie.objects.all().prefetch_related('genre')
    pagination_class = None
    serializer_class = MoviesListSerializer
