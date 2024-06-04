from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.db.models import F 
from django.db.models.functions import Extract
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
            if new_form.entry_date < new_form.end_date:
                objects = Projects.objects.filter(date__range=[new_form.entry_date, new_form.end_date]).order_by('employee_id')
                print(objects)
                name = new_form.name
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename='+ name
                writer = csv.writer(response)
                writer.writerow(['name', 'hours', 'date'])
                for object in objects:
                    writer.writerow([object.employee_id, object.hours, object.date,])
                form.save()
                return response
        else:
            error = 'Неверно введены данные'
            print(error)

    info = Reports.objects.order_by('date')
    print(info)
    form = ReportsForm()

    data = {
        'form': form,
        'info': info,
    }
    return render(request, 'html/reports.html', data)
