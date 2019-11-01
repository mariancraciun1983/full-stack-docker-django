from rest_framework import viewsets
from ..models import Cart
from .serializers import CartCompleteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CartViewSet(viewsets.GenericViewSet):
    http_method_names = ['get', 'head', 'options', 'post']
    permission_classes = (IsAuthenticated,)
    serializer_class = CartCompleteSerializer

    def list(self, request, *args, **kwargs):
        cart = Cart.objects.filter(status=Cart.NEW, user=request.user).first()
        if cart:
            serializer = self.get_serializer(cart)
            return Response(serializer.data)
        else:
            return Response(None)

    def post(self, request, *args, **kwargs):
        pass
