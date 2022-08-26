import traceback

from celery.utils.log import get_task_logger

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.template import loader

from Message_service import celery


logger = get_task_logger(__name__)


@celery.app.task
def send_message(pk):
    from .models import Message

    with transaction.atomic():
        if not (
            message := Message.objects.select_for_update()
            .filter(pk=pk, is_sent=False)
            .first()
        ):
            return
        html_message = loader.render_to_string(
            'message_app/email_message.html', {'message': message}
        )

        try:
            send_mail(
                message.user_report,
                'What is it?',
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                html_message=html_message,
            )
            message.is_sent = True
        except Exception:
            message.send_error = traceback.format_exc()
        message.save()
