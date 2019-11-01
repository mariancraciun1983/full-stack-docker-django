from rest_framework import viewsets
from ..models import Genre
from .serializers import GenresListSerializer
from rest_framework.permissions import AllowAny


class ListViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    permission_classes = (AllowAny,)
    queryset = Genre.objects.all()
    pagination_class = None
    serializer_class = GenresListSerializer
