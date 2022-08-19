from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Message
from .tasks import send_message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'user_name',
            'user_phone',
            'user_email',
            'user_report',
            'text',
        )
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': _('Alexey')}),
            'user_phone': forms.TextInput(
                attrs={'placeholder': '+7(911)111-11-11'}
            ),
            'user_email': forms.TextInput(
                attrs={'placeholder': 'alexey@gmail.com'}
            ),
            'text': forms.Textarea(
                attrs={'placeholder': _('Your message here')}
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit)
        send_message.delay(instance.pk)
        return instance
