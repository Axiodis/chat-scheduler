from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)


class Discount(models.Model):
    discount_code = models.CharField(max_length=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
