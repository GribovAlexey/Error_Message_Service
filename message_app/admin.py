from django.contrib import admin
from .models import Message


class MyAdmin(admin.ModelAdmin):
    list_display = ("user_name", "is_sent")

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.is_sent:
            fields = set(fields)
            fields.remove('sent_error')
        return fields

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(Message, MyAdmin)
