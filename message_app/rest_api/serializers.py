from rest_framework import serializers
from message_app.models import Message
from message_app.tasks import send_message


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'user_name',
            'user_phone',
            'user_email',
            'user_report',
            'text',
        )
