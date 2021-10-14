from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from chats.models import Conversation
from chats.serializers import ChatSerializer


class ConversationSerializer(serializers.ModelSerializer):
    store_id = ReadOnlyField(source="store.id")
    operator_id = ReadOnlyField(source="operator.id")
    operator_group = ReadOnlyField(source="operator.operator_group.name")
    client_id = ReadOnlyField(source="client.id")

    chats = ChatSerializer(many=True, read_only=True, source='chat_set', required=False)

    class Meta:
        model = Conversation
        fields = ['id', 'status', 'store_id', 'operator_group', 'operator_id', 'client_id', 'chats']
