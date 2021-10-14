from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from chats.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    user_id = ReadOnlyField(source="user.id")
    conversation_id = ReadOnlyField(source="conversation.id")

    created_date = serializers.SerializerMethodField('get_created_date')

    def get_created_date(self, obj):
        return obj.created_date.isoformat("T", "seconds")

    class Meta:
        model = Chat
        fields = ['id', 'payload', 'user_id', 'conversation_id', 'status', 'created_date']
