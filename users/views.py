from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/main')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            login = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=login, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/main')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'html/login.html', context)

