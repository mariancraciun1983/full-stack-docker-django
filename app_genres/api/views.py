from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import Genre
from .serializers import GenresListSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ListViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    permission_classes = (AllowAny,)
    queryset = Genre.objects.all()
    pagination_class = None
    serializer_class = GenresListSerializer

    def retrieve(self, request, pk=None):
        if pk.isdigit():
            genre = get_object_or_404(self.queryset, pk=pk)
        else:
            genre = get_object_or_404(self.queryset, slug=pk)
        serializer = GenresListSerializer(genre)
        return Response(serializer.data)
