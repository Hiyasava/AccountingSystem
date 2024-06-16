from django import forms
from message_box.models import Message
from django.contrib.auth import get_user_model

class MessageForm(forms.ModelForm):
    User = get_user_model()
    recipient = forms.ModelChoiceField(queryset=User.objects.all(),label='recipient ')
    text = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text',
        'id': 'text',
        'name': 'text',
        'input': 'text',
        'class': 'text'
    }))
    
    class Meta:
        model = Message
        fields = ('recipient', 'text')