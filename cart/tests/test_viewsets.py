import pytest

from cart.models import Cart


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
