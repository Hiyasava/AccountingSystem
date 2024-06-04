from django.urls import path

from projects.views import projects

app_name='hours'

urlpatterns = [
    path('', projects, name='hours'),
]