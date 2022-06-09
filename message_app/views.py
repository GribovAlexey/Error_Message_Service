from django.contrib import messages
from django.core.mail import send_mail, get_connection
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import MessageForm


def index_view(request):
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            send_message(message_form.cleaned_data)
            messages.success(request, "Report successfully sent")
        else:
            messages.error(request, "Invalid form")

        return redirect('message_app:index')
    message_form = MessageForm()
    return render(request=request, template_name="message_app/index.html",
                  context={'message_form': message_form, })


def send_message(message):
    subject = message['user_report']
    message_text = f"From {message['user_name']} with email {message['user_email']} got message {message['message']}"
    from_email = 'gribov.alexey.m@yandex.ru'
    to = 'gribov.alexey.m@yandex.ru'
    with get_connection() as connection:
        send_mail(subject, message_text, from_email, [to], connection=connection)
