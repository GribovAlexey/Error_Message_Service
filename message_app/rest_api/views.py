from rest_framework.generics import CreateAPIView

from message_app.models import Message
from message_app.rest_api.serializers import MessageSerializer


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
