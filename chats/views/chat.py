from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from chats.models import Chat
from chats.serializers import ChatSerializer

import re


def check_payload_chars(string):
    char_re = re.compile(r'[^a-zA-Z0-9{}$%_\-\\/~@#^&()!? ]')
    string = char_re.search(string)
    return not bool(string)


class ChatViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Chat.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Chat.objects.filter(pk=pk).all()
        chat = get_object_or_404(queryset)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    def create(self, request):
        request_data = request.data.dict()

        if len(request_data['payload']) > 300:
            raise ValidationError('Payload longer then 300', code=None)

        if not check_payload_chars(request_data['payload']):
            raise ValidationError('Payload contains invalid characters', code=None)

        chat = Chat.objects.create(status='NEW', conversation_id=int(request_data['conversation_id']),
                                   discount_id=int(request_data['discount_id']),
                                   user_id=int(request_data['user_id']), payload=request_data['payload'])
        chat.save()

        serializer = ChatSerializer(chat)
        return Response(serializer.data)
