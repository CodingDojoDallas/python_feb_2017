from django.shortcuts import render, redirect
from .models import Course
# Create your views here.

def index(request):
    context = {
        'courses': Course.objects.all()
    }

    return render(request, 'coursesapp/index.html', context)

def add(request):
        Course.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
        return redirect('/')

def delete(request, id):
    context = {
        'courses': Course.objects.get(id = id)
    }
    return render(request, 'coursesapp/delete.html', context)

def destroy(request, id):
    Course.objects.all(), Course.objects.get(id = id).delete
    return redirect('/')
