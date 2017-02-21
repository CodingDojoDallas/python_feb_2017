from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
	context = {
		'CurrentTime' : datetime.now()
	}
	return render(request, 'timedisplay/index.html', context)
	