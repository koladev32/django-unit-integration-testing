import pytest
from django.utils.timezone import now, timedelta

from cart.models import Cart
from discount.models import Discount


@pytest.mark.django_db
def test_cart_model():
    cart = Cart(total=10, currency="USD", items_number=5)
    cart.save()

    assert cart.total == 10
    assert cart.currency == "USD"
    assert cart.items_number == 5


@pytest.mark.django_db
def test_apply_discount_to_cart():
    cart = Cart(total=20, currency="USD", items_number=5)
    cart.save()

    # Creating the discount
    discount = Discount(code="DIS20", value=5, description="Some discount",
                        ended=now() + timedelta(days=2))
    discount.save()

    cart.apply_discount(discount)

    assert cart.amount_discounted == 5
    assert cart.total == 15
    assert cart.total_discounted == 15
