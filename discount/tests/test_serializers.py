from django.utils.timezone import now, timedelta
from discount.serializers import DiscountSerializer


def test_valid_discount_serializer():
    valid_serializer_data = {
        "code": "DIS21",
        "value": 5,
        "description": "Some lines",
        "ended": (now() + timedelta(days=2)).strftime()
    }

    serializer = DiscountSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
