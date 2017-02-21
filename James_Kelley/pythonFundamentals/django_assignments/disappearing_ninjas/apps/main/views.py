from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def ninjas(request):
	return render(request, 'main/ninjas.html')

def colors(request, color):
	context = {
        'color': color
    }
    
	return render(request, 'main/colors.html', context)

