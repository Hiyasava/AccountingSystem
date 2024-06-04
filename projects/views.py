from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from users.views import login
from projects.forms import Project
from projects.models import Project
from django.contrib.auth.decorators import login_required

@login_required()

def projects(request):

    if request.method == 'POST':
        form = Project(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/main')
        else:
            error = 'Неверно введены данные'

    obj = Project.objects.order_by('projects')
    info = obj.filter(employee_id = request.user.username)

    data = {
        'info': info,
    }

    return render(request, 'html/projects.html', data)
