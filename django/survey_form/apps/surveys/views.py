from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import constants as messages
from django.contrib import messages

def index(request):

    return render(request,'surveys/index.html')


def process(request):
    if not request.session['count']:
        request.session['count'] = 0

    errors = []

    if len(request.POST['full_name']) < 1:
        errors.append("Name cannot be empty")
    elif request.POST['location'] == 'selectloc':
        errors.append("Select a location")
    elif request.POST['language'] == 'selectlan':
        errors.append("Select a language")

    if errors:
        for e in errors:
            messages.add_message(request, messages.INFO, e)
        return redirect('/')

    request.session['user'] = request.POST
    request.session['count'] += 1

    messages.add_message(request, messages.INFO, "Thanks for submitting this form! You have submitted this form " + str(request.session['count']) + " time(s) now.")

    return redirect('/result')

def result(request):

    return render(request,'surveys/results.html')
