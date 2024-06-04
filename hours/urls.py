from django.urls import path
from hours.views import hours

app_name='hours'

urlpatterns = [
    path('', hours, name='hours'),
]