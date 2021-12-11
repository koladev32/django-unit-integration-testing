from utils import PaymentAPI
from django.db import models


class Cart(models.Model):
    total = models.FloatField(default=0)
    currency = models.CharField(max_length=5)
    items_number = models.IntegerField(default=0)
    total_discounted = models.FloatField(default=0)
    amount_discounted = models.FloatField(default=0)
    payment_status = models.CharField(default="pending", max_length=35)
    created = models.DateTimeField(auto_now_add=True)

    def apply_discount(self, discount):
        self.amount_discounted += discount.value
        self.total_discounted = self.total - self.amount_discounted

        self.total = self.total_discounted

        self.save(update_fields=['total', 'amount_discounted', 'total_discounted'])

    def pay(self):
        initialized_payment = PaymentAPI()
        payment = initialized_payment.request_payment(cart_id=self.pk, amount=self.total)

        assert payment['cart_id'] == self.pk

        self.payment_status = payment['payment_status']

        self.save(update_fields=['payment_status'])
