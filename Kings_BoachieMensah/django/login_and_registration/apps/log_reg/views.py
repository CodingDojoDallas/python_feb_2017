from django.shortcuts import render, redirect
from .models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'log_reg/index.html')

def create_user(request):
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            first_name = request.POST['f_name'],
            last_name = request.POST['l_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
        )
        request.session['user_id'] = user.id
        return redirect('/success')
    return redirect('/')

def success(request):
    return render(request, 'log_reg/success.html')

def login_user(request):
    login = User.objects.login_user(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        return redirect('/success')
    return redirect('/')
