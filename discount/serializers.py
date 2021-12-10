from django.utils.timezone import now

from rest_framework import serializers
from rest_framework import validators

from discount.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'code', 'description', 'created', 'value', 'created', 'ended',)
        read_only_fields = ('id', 'created',)


class ApplyDiscountSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=35)

    def validate(self, attrs):
        code = attrs.get('code')
        try:
            discount = Discount.objects.get(code=code)
        except Discount.DoesNotExist:
            raise validators.ValidationError("This discount doesn't exist.")

        if discount.ended < now():
            raise validators.ValidationError("This discount has expired.")

        return attrs
