from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0

    location = [
        'Mountain View',
        'Dallas',
        'Seattle',
        'Washington, D.C.',
        'Los Angeles',
    ]

    language = [
        'JavaScript',
        'Ruby',
        'C#',
        'Python',
    ]

    context = {
        'location': location,
        'language': language,
    }

    return render(request, 'surveyform/index.html', context)

def create(request):
    request.session['count'] += 1
    if request.method == 'POST':
        request.session['whole_name'] = request.POST['whole_name']
        request.session['fav_lang'] = request.POST['fav_lang']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def show(request):
    if request.method == 'POST':
        request.session['go_back'] = request.POST['go_back']
        return redirect('/')
    else:
        return render(request, 'surveyform/show.html')
