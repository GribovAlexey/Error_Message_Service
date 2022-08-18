import traceback

from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

from Message_service import celery
from .models import Message

logger = get_task_logger(__name__)


@celery.app.task
def send_message(pk):
    if not (message := Message.objects.get(pk=pk)):
        return
    html_message = loader.render_to_string(
        'message_app/email_message.html',
        {
            'subject': message.get_user_report_display(),
            'user_name': message.user_name,
            'user_email': message.user_email,
            'user_phone': message.user_phone,
            'message': message.text,
        }
    )

    try:
        send_mail(message.user_report, 'What is it?',
                  settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER],
                  html_message=html_message)
        message.message_send = True
    except Exception:
        message.message_send_error = traceback.format_exc()
        message.save()
