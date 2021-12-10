import pytest

from cart.models import Cart


@pytest.mark.django_db
def test_cart_model():
    cart = Cart(total=10, currency="USD", items_number=5)
    cart.save()

    assert cart.total == 10
    assert cart.currency == "USD"
    assert cart.items_number == 5
