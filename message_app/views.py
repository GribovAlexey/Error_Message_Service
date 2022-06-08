from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import MessageForm


# Create your views here.
def index_view(request):
    if request.method == "POST":
        print("here")
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            messages.success(request, "Report successfully sent")
        else:
            messages.error(request, "Invalid form")

        return redirect('message_app:index')
    message_form = MessageForm()
    return render(request=request, template_name="message_app/index.html",
                  context={'message_form': message_form, })
