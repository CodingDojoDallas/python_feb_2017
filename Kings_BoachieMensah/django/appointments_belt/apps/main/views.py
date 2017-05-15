from django.shortcuts import render, redirect
from .models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def create_user(request):
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
            date_of_birth = request.POST['date_of_birth'],
        )
        request.session['user_id'] = user.id
        return redirect('/appointments')
    return redirect('/')

def login_user(request):
    login = User.objects.login_user(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        return redirect('/appointments')
    return redirect('/')

def update_appt(request, id):
    return redirect('/appointments')
