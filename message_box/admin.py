from django.contrib import admin
from message_box.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
