from django.apps import AppConfig
from django.contrib import admin
from reports.models import Reports, generatedReports

admin.site.register(Reports)
admin.site.register(generatedReports)