import json

import pytest

from django.utils.timezone import now, timedelta
from discount.models import Discount


@pytest.mark.django_db
def test_add_discount(client):
    discounts = Discount.objects.all()
    assert discounts.count() == 0

    response = client.post(
        "/api/discount/",
        {
            "code": "DIS21",
            "value": 5,
            "description": "Some lines",
            "ended": (now() + timedelta(days=2))
        },
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.data['code'] == "DIS21"

    discounts = Discount.objects.all()
    assert discounts.count() == 1
