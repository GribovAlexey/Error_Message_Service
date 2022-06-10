import traceback

from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

import my_celery
from .models import Message

logger = get_task_logger(__name__)


@my_celery.app.task
def send_message(pk):
    my_message = Message.objects.get(pk=pk)
    subject = my_message.user_report
    message_text = f"From {my_message.user_name} with email " \
                   f"{my_message.user_email} got message {my_message.message}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = settings.EMAIL_HOST_USER
    try:
        send_mail(subject, message_text, from_email, [to])
    except Exception:
        my_message.message_send = False
        my_message.message_send_error = traceback.format_exc()
