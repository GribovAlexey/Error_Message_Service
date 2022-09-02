from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .context_processor import user_count
from .forms import MessageForm
from .tasks import send_message


def index_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save()
            send_message.delay(instance.pk)
            messages.success(request, _("Report successfully sent"))
        else:
            messages.error(request, _("Invalid form"), extra_tags='danger')
    else:
        form = MessageForm()
    return render(
        request=request,
        template_name="message_app/message_forms.html",
        context={
            'form': form,
            'user_amount': user_count(request),
        },
    )
