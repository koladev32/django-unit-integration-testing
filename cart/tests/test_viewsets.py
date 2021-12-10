import pytest
from django.utils.timezone import now, timedelta
from cart.models import Cart
from discount.models import Discount


@pytest.mark.django_db
def test_add_cart(client):
    carts = Cart.objects.all()
    assert carts.count() == 0

    response = client.post(
        "/api/cart/",
        {
            "total": 10,
            "currency": "USD",
            "items_number": 5
        },
        content_type="application/json"
    )

    assert response.status_code == 201

    carts = Cart.objects.all()
    assert carts.count() == 1


@pytest.mark.django_db
def test_get_all_carts(client):
    response = client.get(
        "/api/cart/",
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve_cart(client):
    response = client.post(
        "/api/cart/",
        {
            "total": 10,
            "currency": "USD",
            "items_number": 5
        },
        content_type="application/json"
    )
    assert response.status_code == 201

    response_data = response.data

    response = client.get(
        f"/api/cart/{response_data['id']}/",
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_apply_discount_to_cart(client):
    # CREATING THE DISCOUNT
    discount = Discount(code="DIS20", value=5, description="Some discount",
                        ended=now() + timedelta(days=2))
    discount.save()

    response = client.post(
        "/api/cart/",
        {
            "total": 20,
            "currency": "USD",
            "items_number": 5
        },
        content_type="application/json"
    )
    assert response.status_code == 201

    response_data = response.data

    response = client.post(
        f"/api/cart/{response_data['id']}/apply_discount/",
        {
            "code": "DIS20"
        },
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data['total'] == 15
    assert response.data['total_discounted'] == 15
    assert response.data['amount_discounted'] == 5

