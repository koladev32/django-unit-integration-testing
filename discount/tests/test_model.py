import pytest

from django.utils.timezone import now, timedelta
from discount.models import Discount


@pytest.mark.django_db
def test_discount_model():
    discount = Discount(code="DIS20", value=5, description="Some discount",
                        created=now(), ended=now() + timedelta(days=2))
    discount.save()

    assert discount.code == "DIS20"
    assert discount.created < discount.ended
    assert discount.value == 5
