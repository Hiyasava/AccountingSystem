from django.forms import ModelForm
from django import forms

from main.models import News

class MainForm(ModelForm):

    image = forms.ImageField(required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text',
        'id': 'text',
        'name': 'text',
        'input': 'text',
        'class': 'text'
    }))
    

    class Meta:
        model = News
        fields = ('image', 'text')
