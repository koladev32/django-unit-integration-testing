from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from discount.serializers import DiscountSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = DiscountSerializer
    permission_classes = (AllowAny,)
