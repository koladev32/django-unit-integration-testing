from django.db import models


class Cart(models.Model):
    total = models.FloatField(default=0)
    currency = models.CharField(max_length=5)
    items_number = models.IntegerField(default=0)
    total_discounted = models.FloatField(default=0)
    amount_discounted = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
