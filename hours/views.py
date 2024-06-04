from django.shortcuts import render,redirect
from hours.forms import ProjectsForm
from hours.models import Projects


from django.contrib.auth.decorators import login_required

@login_required()
def hours(request):
    error = ''
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.employee_id = request.user.username
            new_form.save()
            return redirect('/main')
        else:
            error = 'Неверно введены данные'


           
    obj = Projects.objects.all().order_by('-date')
    info = obj.filter(employee_id = request.user.username)
    form = ProjectsForm()

    data = {
        'form': form,
        'error': error,
        'info': info,
    }

    return render(request, 'html/hours.html', data)
