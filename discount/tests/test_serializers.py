import pytest

from django.utils.timezone import now, timedelta
from discount.serializers import DiscountSerializer, ApplyDiscountSerializer
from discount.models import Discount


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


@pytest.mark.django_db
def test_apply_discount_serializer():
    # CREATING THE DISCOUNT
    discount = Discount(code="DIS20", value=5, description="Some discount",
                        created=now(), ended=now() + timedelta(days=2))
    discount.save()

    discount_data = {
        "code": "DIS20"
    }

    serializer = ApplyDiscountSerializer(data=discount_data)
    assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_apply_expired_discount_serializer():
    # CREATING THE DISCOUNT
    discount = Discount(code="DIS19", value=5, description="Some discount",
                        created=now(), ended=now() - timedelta(days=2))
    discount.save()

    discount_data = {
        "code": "DIS19"
    }

    serializer = ApplyDiscountSerializer(data=discount_data)
    assert not serializer.is_valid()


@pytest.mark.django_db
def test_apply_non_exist_discount_serializer():
    discount_data = {
        "code": "DIS32"
    }

    serializer = ApplyDiscountSerializer(data=discount_data)
    assert not serializer.is_valid()
