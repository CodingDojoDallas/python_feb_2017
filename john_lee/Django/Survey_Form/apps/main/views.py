from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def show(request):
    if 'display_attempt' not in request.session:
        request.session['display_attempt'] = 0
    else:
        request.session['display_attempt'] = request.session['display_attempt'] + 1
    return render(request, 'main/show.html')

def create(request):
    print(request.method)
    if request.method  == "POST":
        request.session['name'] = request.POST['user_name']
        request.session['dojo'] = request.POST['dojo_location']
        request.session['language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['submit_comment']
        return redirect('/users')
    else:
        return redirect('/')
