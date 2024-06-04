from hours.models import Projects
from django.forms import ModelForm
from django import forms

from hours.models import Projects

class ProjectsForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'id': 'date',
        'name': 'date',
        'input': 'date'
    }))
    hours = forms.IntegerField(widget=forms.TextInput(attrs={
        'type': 'number',
        'id': 'dtime',
        'name': 'time',
        'input': 'time',
        'maxlength': '3'
    }))
    projects = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'project',
        'name': 'project',
        'input': 'project'
    }))

    class Meta:
        model = Projects
        fields = ('date','hours','projects')