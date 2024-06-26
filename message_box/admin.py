from django.contrib import admin
from message_box.models import Message
from django_summernote.admin import SummernoteModelAdmin

class MessageAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Message, MessageAdmin)
