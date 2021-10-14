from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from chats.models import Conversation
from chats.serializers import ConversationSerializer


class ConversationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Conversation.objects.all()
        serializer = ConversationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.filter(pk=pk).all()
        conversation = get_object_or_404(queryset)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)

    def create(self, request):
        request_data = request.data.dict()

        conversation = Conversation.objects.create(status='NEW', operator_id=int(request_data['operator_id']),
                                                   client_id=int(request_data['client_id']),
                                                   store_id=int(request_data['store_id']))
        conversation.save()

        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)
