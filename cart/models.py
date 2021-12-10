from django.db import models


class Cart(models.Model):
    total = models.FloatField(default=0)
    currency = models.CharField(max_length=5)
    items_number = models.IntegerField(default=0)
    total_discounted = models.FloatField(default=0)
    amount_discounted = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def apply_discount(self, discount):

        self.amount_discounted += discount.value
        self.total_discounted = self.total - self.amount_discounted

        self.total = self.total_discounted

        self.save(update_fields=['total', 'amount_discounted', 'total_discounted'])


