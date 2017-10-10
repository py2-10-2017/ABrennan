from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from django.utils import timezone


def index(request):
    start = timezone.localtime(timezone.now())
    time = {
        'now':start.strftime("%I:%M%p on %B %d, %Y ")
    }

    return render(request,'words/index.html', time)


def add(request):
    errors = []

    if len(request.POST['word']) < 1:
        errors.append("Word cannot be empty")

    if errors:
        for e in errors:
            messages.add_message(request, messages.INFO, e)
        return redirect('/')

    try:
        request.session['newWords']
    except KeyError:
        request.session['newWords'] = []

    temp = request.session['newWords']
    temp.append(request.POST)
    request.session['words'] = temp

    return redirect('/')


def clear(request):

    del request.session['newWords']

    return redirect('/')
