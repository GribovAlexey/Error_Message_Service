from django.core.validators import RegexValidator
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from message_app.tasks import send_message


phone_validation = RegexValidator(
    regex=r"[+]\d[(]\d{3}[)]\d{3}[-]\d{2}[-]\d{2}",
    message=_("Use correct format for phone field!"),
    code="invalid_regex",
)


class Message(models.Model):
    class ReportType(models.TextChoices):
        RECEIVE_ERROR = "RE", _("Receive error")
        SEND_ERROR = "SE", _("Send error")
        OTHER_ERROR = "OE", _("Other error")

    user_name = models.CharField(
        _("name"),
        max_length=30,
    )
    user_phone = models.CharField(
        _("phone"), max_length=20, validators=[phone_validation]
    )
    user_email = models.EmailField(_("email"))
    user_report = models.CharField(
        _("report type"),
        max_length=2,
        choices=ReportType.choices,
        default=ReportType.OTHER_ERROR,
    )
    text = models.TextField(_("message"), max_length=10000)
    is_sent = models.BooleanField(
        default=False,
    )
    send_error = models.TextField(
        editable=False,
    )

    def __str__(self):
        return f"Message from {self.user_name}"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.send_mail_async()
        super().save(force_insert, force_update, using, update_fields)

    def send_mail_async(self):
        if not self.is_sent:
            transaction.on_commit(lambda: send_message.delay(self.pk))
