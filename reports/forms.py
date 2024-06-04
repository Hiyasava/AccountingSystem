from reports.models import Reports
from django.forms import ModelForm
from django import forms


class ReportsForm(ModelForm):

    entry_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'id': 'startDate',
        'name': 'date',
        'input': 'date',
    }))
    end_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'id': 'endDate',
        'name': 'date',
        'input': 'date'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'type',
        'name': 'type',
        'input': 'type'
    }))

    class Meta:
        model = Reports
        fields = ('entry_date','end_date','name')
        exclude = ['link']