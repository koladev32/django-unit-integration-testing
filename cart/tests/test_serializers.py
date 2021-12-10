import pytest

from cart.serializers import CartSerializer


@pytest.mark.django_db
def test_valid_cart_serializer():
    valid_serializer_data = {
        "total": 10,
        "currency": "USD",
        "items_number": 5,
    }

    serializer = CartSerializer(data=valid_serializer_data)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.validated_data == valid_serializer_data
