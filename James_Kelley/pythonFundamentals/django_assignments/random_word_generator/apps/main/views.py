from django.shortcuts import render
import random
import string

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    rand_word = ""
    for x in range(14):
        if random.random() > 0.4: #output more letters than numbers
            rand_word += random.choice(string.letters)
        else:
            rand_word += str(random.randrange(0,10))
    context = {
        'word': rand_word
    }
    return render(request, 'main/index.html', context)
