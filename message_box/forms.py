from django import forms
from message_box.models import Message
from django.contrib.auth import get_user_model
from django_summernote.admin import SummernoteWidget, SummernoteInplaceWidget

class MessageForm(forms.ModelForm):
    User = get_user_model()
    recipient = forms.ModelChoiceField(queryset=User.objects.all(),label='Получатель')
    widgets = {
    'recipients' : forms.Select(attrs={
        'class' : "dropdown-list",
        'label': 'Получатель'
    }),
}
    text = forms.CharField(widget=SummernoteWidget(attrs={
        'type': 'text',
        'class': 'message'
    }))

    label = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'text',
        'name': 'text',
        'input': 'text',
        'class': 'message_label'
    }))
    
    class Meta:
        model = Message
        fields = ('recipient', 'text', 'label')