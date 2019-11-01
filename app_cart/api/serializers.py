from rest_framework import serializers
from ..models import Cart, CartItems


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'status', 'created', 'updated']

class CartItemsSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    def get_movie(self, obj):
        return str(obj.movie)

    class Meta:
        model = CartItems
        fields = ['quantity', 'movie']

class CartCompleteSerializer(CartSerializer):
    movies = serializers.SerializerMethodField(required=False)

    def get_movies(self, cart):
        items = CartItems.objects.filter(cart=cart).values_list('quantity', 'movie', named=True)
        serializer = CartItemsSerializer(items, many=True)
        return serializer.data

    class Meta(CartSerializer.Meta):
        fields = CartSerializer.Meta.fields + ['movies']
