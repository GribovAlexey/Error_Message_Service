from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


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
        (RECEIVE_ERROR, _("Receive error")),
        (SEND_ERROR, _("Send error")),
        (OTHER_ERROR, _("Other error")),
    ]
    user_name = models.CharField(_("name"), max_length=30, )
    user_phone = models.CharField(_("phone"),max_length=20, validators=[phone_validation])
    user_email = models.EmailField(_('email'))
    user_report = models.CharField(
        _("report type"),
        max_length=2,
        choices=report_type,
        default=OTHER_ERROR,
    )
    message = models.TextField(_('message'))
    message_sent = models.BooleanField(default=True, )
    message_sent_error = models.TextField(default="", )

    def __str__(self):
        return f"Message from {self.user_name}"
