import re

from chats.models import Chat
from chatscheduler import celery_app
from chatscheduler.custom_settings import CHATS_PER_HOUR_LIMIT


@celery_app.task(bind=True, rate_limit=f'{CHATS_PER_HOUR_LIMIT}/h')
def send_chat(self, chat_id):
    chat: Chat = Chat.objects.filter(pk=chat_id).first()

    payload = chat.payload

    payload = re.sub(r"{{\s*client\.first_name\s*}}", chat.conversation.client.user.first_name, payload)
    payload = re.sub(r"{{\s*operator\.full_name\s*}}",
                     f"{chat.conversation.client.user.first_name} {chat.conversation.client.user.last_name}", payload)
    payload = re.sub(r"{{\s*discount\.discount_code\s*}}", chat.discount.discount_code, payload)

    print(payload)

    chat.status = 'SENT'
    chat.save()
