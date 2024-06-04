from django.urls import path

from reports.views import reports

app_name='reports'

urlpatterns = [
    path('', reports, name='reports')
]