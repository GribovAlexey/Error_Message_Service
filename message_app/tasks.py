from celery import Celery
from celery.utils.log import get_task_logger

from django.core.mail import send_mail

from Message_service.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_USER

app = Celery('sending_task', broker='redis://localhost:6379/0')
logger = get_task_logger(__name__)


@app.task
def send_message(message):
    subject = message['user_report']
    message_text = f"From {message['user_name']} with email {message['user_email']} got message {message['message']}"
    from_email = DEFAULT_FROM_EMAIL
    to = EMAIL_HOST_USER
    send_mail(subject, message_text, from_email, [to])
