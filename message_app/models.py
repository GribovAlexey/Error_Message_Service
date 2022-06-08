from django import forms
from django.db import models


# Create your models here.
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
    user_phone = models.CharField(max_length=15, )
    user_email = models.EmailField()
    user_report = models.CharField(
        max_length=2,
        choices=report_type,
        default=OTHER_ERROR,
    )
    message = models.TextField()
