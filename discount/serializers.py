from rest_framework import serializers

from discount.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'code', 'description', 'created', 'value', 'created', 'ended',)
        read_only_fields = ('id', 'created',)
