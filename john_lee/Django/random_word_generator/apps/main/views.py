from django.shortcuts import render, redirect
import random
import string
# Create your views here.
def index(request):
    if 'display_generated' not in request.session:
        request.session['display_attempt'] = 0
    else:
        request.session['display_attempt'] = request.session['display_attempt'] + 1
	return render(request, 'main/index.html')


def generate(request):
    print(request.method)
    if request.method == "POST":
        generated = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
        request.session['display_generated'] = generated
        return redirect('/')
    else:
        return redirect('/')
