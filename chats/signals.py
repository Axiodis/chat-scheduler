from datetime import datetime, timedelta

import pytz
from django.db.models.signals import post_save
from django.dispatch import receiver

# method for updating
from chats.models import Chat, Schedule
from .tasks import send_chat


@receiver(post_save, sender=Chat, dispatch_uid="schedule_send_chat")
def schedule_send_chat(sender, instance: Chat, **kwargs):
    timezone = instance.conversation.client.timezone or instance.conversation.store.timezone

    now = datetime.utcnow()

    utc_timezone = pytz.timezone("UTC")
    user_timezone = pytz.timezone(timezone)

    now_localized = now.astimezone(user_timezone)

    eta = None
    if now_localized.hour >= 20:
        eta = (now_localized + timedelta(days=1)).replace(hour=9, minute=1, second=0, microsecond=0)
        eta = eta.astimezone(utc_timezone)

    if 0 <= now_localized.hour < 9:
        eta = now_localized.replace(hour=9, minute=1, second=0, microsecond=0)
        eta = eta.astimezone(utc_timezone)

    if eta is None:
        eta = datetime.utcnow() + timedelta(minutes=1)

    schedule = Schedule.objects.create(chat_id=instance.id, sending_date=eta)
    schedule.save()

    send_chat.apply_async((instance.id,), eta=eta)
