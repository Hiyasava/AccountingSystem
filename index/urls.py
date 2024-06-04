from django.urls import path
from index.views import index_

app_name='index'

urlpatterns = [
    path('', index_, name='index')
]