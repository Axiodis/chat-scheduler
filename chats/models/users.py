from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    timezone = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OperatorGroup(models.Model):
    name = models.CharField(max_length=50)


class Operator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operator_group = models.ForeignKey(OperatorGroup, on_delete=models.CASCADE)
