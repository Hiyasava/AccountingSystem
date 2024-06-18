from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notes.models import Note

@login_required
def view_message(request, pk):
    message = Note.objects.get(pk=pk)
    return render(request, 'view_message.html', {'message': message})