from rest_framework import viewsets
from message_app.rest_api.serializers import MessagesSerializer
from message_app.models import Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
