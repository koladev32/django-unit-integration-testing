from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from cart.serializers import CartSerializer
from cart.models import Cart
from discount.serializers import ApplyDiscountSerializer


class CartViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = CartSerializer
    permission_classes = (AllowAny,)
    queryset = Cart.objects.all()

    @action(methods=['post'], detail=True)
    def apply_discount(self, request, pk=None):
        obj = self.get_object()

        serializer = ApplyDiscountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj.apply_discount(serializer.validated_data['discount'])

        return Response(CartSerializer(obj).data, status=status.HTTP_200_OK)