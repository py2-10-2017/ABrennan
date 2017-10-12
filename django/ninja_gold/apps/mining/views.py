from django.shortcuts import render, redirect
from locations import locations
from quotes import quotes
import random
import time

def index(request):

    try:
        request.session['check']
    except KeyError:
        request.session['check'] = 'winner'
        request.session['position'] = '50%'
        request.session['out'] = ''

    if request.session['gold'] < 0:
        request.session['check'] = 'loser'

    r = random.randint(0, len(quotes)-1)
    q = list(quotes[r])

    context = {
        'locations': locations,
        'quote': q
    }

    return render(request, 'mining/index.html', context)

def reset(request):
    request.session['position'] = '50%'
    request.session['out'] = ''
    request.session['check'] = 'winner'
    request.session['gold'] = 0

    return redirect('/')

def process(request, location):

    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0

    now = time.strftime("%m/%d/%Y %I:%M %p")

    for x in locations:
        if x['name'] == location:
            newGold = random.randint(x['min'], x['max'])
            request.session['position'] = x['position']

    request.session['gold'] += newGold

    if newGold < 0:
        request.session['out'] += '<p class="red">Entered a casino and lost ' + str(newGold) + ' tokens - (' + now + ')</p>'
    else:
        request.session['out'] += '<p class="green">Entered a ' + location + ' and won ' + str(newGold) + ' gold tokens - (' + now + ')</p>'

    return redirect('/')
