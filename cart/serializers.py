from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'total', 'total_discounted', 'amount_discounted', 'items_number', 'created', 'currency',)
        read_only_fields = ('id', 'total_discounted', 'amount_discounted', 'created',)
