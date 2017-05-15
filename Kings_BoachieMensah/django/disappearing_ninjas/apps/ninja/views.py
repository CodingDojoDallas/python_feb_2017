from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'ninja/index.html')

def show_ninja(request, ninja_color):
    print ninja_color

    if ninja_color == '':
        request.session['images'] = '/../../static/ninja/images/tmnt.png'

    elif ninja_color == 'blue':
        request.session['images'] = '/../../static/ninja/images/leonardo.jpg'

    elif ninja_color == 'orange':
        request.session['images'] = '/../../static/ninja/images/michelangelo.jpg'

    elif ninja_color == 'red':
        request.session['images'] = '/../../static/ninja/images/raphael.jpg'

    elif ninja_color == 'purple':
        request.session['images'] = '/../../static/ninja/images/donatello.jpg'

    else:
        request.session['images'] = '/../../static/ninja/images/notapril.jpg'

    return render(request, 'ninja/show_ninja.html')
