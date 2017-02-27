from django.shortcuts import render, HttpResponse, redirect
# CONTROLLER
# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def show_users(request):
    print request.method
    return render(request, "first_app/show_users.html")

def create(request):
    if request.method == "POST":
        print "*" * 50
        print request.POST
        print request.method
        print "*" * 50
        request.session["f_name"] = request.POST["first_name"]
        request.session["l_name"] = request.POST["last_name"]
        return redirect("/")
    else:
        return redirect("/")
