from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import MessageForm
from .tasks import send_message


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


'''
def send_message(message):
    subject = message['user_report']
    message_text = f"From {message['user_name']} with email {message['user_email']} got message {message['message']}"
    from_email = DEFAULT_FROM_EMAIL
    to = EMAIL_HOST_USER
    with get_connection() as connection:
        send_mail(subject, message_text, from_email, [to], connection=connection)
'''
