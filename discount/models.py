from django.db import models


class Discount(models.Model):
    code = models.CharField(max_length=35, unique=True, db_index=True)
    value = models.FloatField()
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField()
