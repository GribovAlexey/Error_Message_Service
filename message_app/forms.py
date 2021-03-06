from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'user_name',
            'user_phone',
            'user_email',
            'user_report',
            'message',
        )
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': _('Alexey')}),
            'user_phone': forms.TextInput(
                attrs={'placeholder': '+7(911)111-11-11'}),
            'user_email': forms.TextInput(
                attrs={'placeholder': 'alexey@gmail.com'}),
            'message': forms.Textarea(
                attrs={'placeholder': _('Your message here')}),
        }
