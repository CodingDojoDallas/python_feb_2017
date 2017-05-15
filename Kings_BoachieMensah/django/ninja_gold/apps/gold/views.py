from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'ninja_gold' not in request.session:
        request.session['ninja_gold'] = 0
    return render(request, 'gold/index.html')

def process(request):
    stat = 'stat'
    begin = 0;
    farm = random.randrange(10,20);
    cave = random.randrange(5,10);
    house = random.randrange(2,5);
    casino = random.randrange(-50,50);

    if request.POST.get['farm']:
        request.session['your_gold'] += farm
        request.session['won_gold'] = 'You have won {} gold!'.format(farm)
        return redirect('/')

    elif request.POST.get['cave']:
        request.session['your_gold'] += cave
        request.session['won_gold'] = 'You have won {} gold!'.format(cave)
        return redirect('/')

    elif request.POST.get['house']:
        request.session['your_gold'] += house
        request.session['won_gold'] = 'You have won {} gold!'.format(house)
        return redirect('/')

    elif request.POST.get['casino']:
        request.session['your_gold'] += casino
        if casino < 0:
            request.session['lost_gold'] = 'You have lost {} gold!'.format(casino)
        if casino > 0:
            request.session['won_gold'] = 'You have won {} gold!'.format(casino)
        return redirect('/')

    elif request.POST.get['reset_game']:
        request.session['your_gold'] = 0
        request.session['won_gold'] = ''
        request.session['lost_gold'] = ''
        request.session['max'] = 0
        request.session['min'] = 0
        request.session.clear()
        request.session['luck'] = 'Good Luck!'
        return redirect('/')
