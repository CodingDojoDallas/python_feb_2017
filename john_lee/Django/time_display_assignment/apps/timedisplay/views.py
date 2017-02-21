from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    context = {
    "today": datetime.now()
    }
    return render(request,'timedisplay/index.html', context)
