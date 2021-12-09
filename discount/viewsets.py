from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from discount.serializers import DiscountSerializer
from discount.models import Discount


class DiscountViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = DiscountSerializer
    permission_classes = (AllowAny,)
    queryset = Discount.objects.all()
