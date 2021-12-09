import pytest

from django.utils.timezone import now, timedelta
from discount.serializers import DiscountSerializer


@pytest.mark.django_db
def test_valid_discount_serializer():
    valid_serializer_data = {
        "code": "DIS21",
        "value": 5,
        "description": "Some lines",
        "ended": (now() + timedelta(days=2))
    }

    serializer = DiscountSerializer(data=valid_serializer_data)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.validated_data == valid_serializer_data
