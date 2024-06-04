from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from main.forms import MainForm
from main.models import News

@login_required()
def main(request):

    info = News.objects.all()
    

    data = {
        'info': info,
    }

    return render(request, 'html/main.html', data)