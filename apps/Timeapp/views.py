
from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime


# Create your views here.
def index(request):
    date = datetime.now().date().strftime('%B %-d, %Y')
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request, 'Timeapp/index.html', context) # updated this line
