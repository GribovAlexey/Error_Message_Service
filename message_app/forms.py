from django import forms
from .models import Message


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
            'user_name': forms.TextInput(attrs={'placeholder': 'Alexey'}),
            'user_phone': forms.TextInput(
                attrs={'placeholder': '+7(911)111-11-11'}),
            'user_email': forms.TextInput(
                attrs={'placeholder': 'alexey@gmail.com'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Your message here'}),
        }
