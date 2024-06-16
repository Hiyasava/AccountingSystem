from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from message_box.models import Message
from message_box.forms import MessageForm

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'inbox.html', {'messages': messages})

@login_required
def outbox(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'outbox.html', {'messages': messages})

@login_required
def compose(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'compose.html', {'form': form})

@login_required
def view_message(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request, 'view_message.html', {'message': message})