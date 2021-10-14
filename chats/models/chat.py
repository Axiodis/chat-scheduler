from django.db import models

from chats.models.store import Store, Discount
from chats.models.users import Client, Operator

from django.contrib.auth.models import User


class Conversation(models.Model):
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    operator = models.ForeignKey(Operator, on_delete=models.RESTRICT)
    status = models.CharField(max_length=50, default='NEW')


class Chat(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.RESTRICT)
    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    status = models.CharField(max_length=50, default='NEW')
    payload = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)


class Schedule(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.RESTRICT)
    sending_date = models.DateTimeField()
