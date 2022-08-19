from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .forms import MessageForm
from .tasks import send_message


def index_view(request):
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            instance = message_form.save()
            send_message.delay(instance.pk)
            messages.success(request, _("Report successfully sent"))
        else:
            messages.error(request, _("Invalid form"), extra_tags='danger')
    else:
        message_form = MessageForm()
    return render(
        request=request,
        template_name="message_app/message_forms.html",
        context={
            'message_form': message_form,
        },
    )
