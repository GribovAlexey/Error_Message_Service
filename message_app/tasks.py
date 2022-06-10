import traceback

from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

import my_celery
from .models import Message

logger = get_task_logger(__name__)


@my_celery.app.task
def send_message(pk):
    my_message = Message.objects.get(pk=pk)
    print()
    html_message = loader.render_to_string(
        'message_app/email_message.html',
        {
            'subject': my_message.get_user_report_display(),
            'user_name': my_message.user_name,
            'user_email': my_message.user_email,
            'user_phone': my_message.user_phone,
            'message': my_message.message,
        }
    )

    subject = my_message.user_report
    message = 'What is it?'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = settings.EMAIL_HOST_USER
    try:
        send_mail(subject, message, from_email, [to], html_message=html_message)
    except Exception:
        my_message.message_send = False
        my_message.message_send_error = traceback.format_exc()
