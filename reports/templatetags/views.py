from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from reports.forms import ReportsForm
from reports.models import Reports, generatedReports

from hours.models import Projects

from datetime import datetime, date
import csv

@login_required()
def reports(request):

    
    if request.method == 'POST':
        form = ReportsForm(request.POST)
    

        if form.is_valid():
            new_form = form.save(commit=False)
            objects = Projects.objects.all()
            name = new_form.name
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename='+ name
            writer = csv.writer(response)
            writer.writerow(['name', 'hours', 'date'])
            for object in objects:
                writer.writerow([object.employee_id, object.hours, object.date])
            form.save()
            return response
        else:
            error = 'Неверно введены данные'
            print(error)

    info = Reports.objects.all()
    form = ReportsForm()

    data = {
        'form': form,
        'info': info,
    }
    return render(request, 'html/reports.html', data)
