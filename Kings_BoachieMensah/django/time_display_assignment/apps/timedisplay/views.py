from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "time":"February 19, 2017",
        "date":"3:46 PM"
    }
    return render(request, 'timedisplay/index.html', context)
