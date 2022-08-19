from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from .forms import MessageForm


class MessageFormView(SuccessMessageMixin, CreateView):
    template_name = 'message_app/message_forms.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_app:class_view')
    success_message = "Your report was sent successfully"

    def form_invalid(self, form):
        messages.error(self.request, _("Invalid form"), extra_tags='danger')
        return super().form_invalid(form)
