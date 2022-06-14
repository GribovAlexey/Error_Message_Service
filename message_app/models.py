from django.db import models
from django.core.validators import RegexValidator

phone_validation = RegexValidator(
    regex=r'[+]\d[(]\d{3}[)]\d{3}[-]\d{2}[-]\d{2}',
    message='Use correct format for phone field!',
    code='invalid_regex',
    )


class Message(models.Model):
    RECEIVE_ERROR = "RE"
    SEND_ERROR = "SE"
    OTHER_ERROR = "OE"
    report_type = [
        (RECEIVE_ERROR, "Receive error"),
        (SEND_ERROR, "Send error"),
        (OTHER_ERROR, "Other error"),
    ]
    user_name = models.CharField(max_length=30, )
    user_phone = models.CharField(max_length=20, validators=[phone_validation])
    user_email = models.EmailField()
    user_report = models.CharField(
        max_length=2,
        choices=report_type,
        default=OTHER_ERROR,
    )
    message = models.TextField()
    message_sent = models.BooleanField(default=True, )
    message_sent_error = models.TextField(default="", )
