from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'label': 'Логин',
        'class':'input-field', 
        'placeholder':'Введите логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'label': 'Пароль',
        'class':'input-field', 
        'placeholder':'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username',
                   'password'
        )
