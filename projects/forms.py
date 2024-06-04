from django.forms import ModelForm
from django import forms

from projects.models import Project

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
    project = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'project',
        'name': 'project',
        'input': 'project'
    }))
    state = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'state',
        'name': 'state',
        'input': 'state'
    }))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'comment',
        'name': 'comment',
        'input': 'comment'
    }))

    class Meta:
        model = Project
        fields = ('hours','projects', 'state', 'comment')