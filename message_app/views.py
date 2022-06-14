from django.contrib import messages
from django.shortcuts import render

from .forms import MessageForm
from .tasks import send_message

'''
def index_view(request):
    message_form = MessageForm(request.POST)
    if message_form.is_valid():
        instance = message_form.save()
        send_message.delay(instance.pk)
        messages.success(request, "Report successfully sent")
    else:
        messages.error(request, "Invalid form")
    return render(request=request,
                  template_name="message_app/index.html",
                  context={'message_form': message_form, })
'''


def index_view(request):
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            instance = message_form.save()
            send_message.delay(instance.pk)
            messages.success(request, "Report successfully sent")
        else:
            messages.error(request, "Invalid form", extra_tags='danger')
    else:
        message_form = MessageForm()
    return render(request=request, template_name="message_app/index.html",
                  context={'message_form': message_form, })
