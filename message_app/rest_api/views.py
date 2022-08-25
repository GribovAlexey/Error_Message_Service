from rest_framework.generics import CreateAPIView
from message_app.rest_api.serializers import MessagesSerializer
from message_app.models import Message


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
