from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from cart.serializers import CartSerializer
from cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = CartSerializer
    permission_classes = (AllowAny,)
    queryset = Cart.objects.all()
