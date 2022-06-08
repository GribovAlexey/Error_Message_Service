from django import forms
from django.contrib import messages
from django.db import models
from django.core.mail import send_mail, BadHeaderError

# Create your models here.
from django.http import request
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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

    def send_message(self):
        subject = self.user_report
        html_message = render_to_string('mail_template.html',
                                        {'context': 'values'})
        plain_message = strip_tags(html_message)
        from_email = 'From <from@example.com>'
        to = 'to@example.com'

        send_mail(subject, plain_message, from_email, [to],
                  html_message=html_message)
