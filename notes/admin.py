from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from notes.models import Note

class NoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Note, NoteAdmin)
