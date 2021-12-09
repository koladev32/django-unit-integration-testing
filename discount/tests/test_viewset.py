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


@pytest.mark.django_db
def test_get_all_discounts(client):
    response = client.get(
        "/api/discount/",
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve_discount(client):

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

    response_data = response.data

    response = client.get(
        f"/api/discount/{response_data['id']}/",
    )

    assert response.status_code == 200
