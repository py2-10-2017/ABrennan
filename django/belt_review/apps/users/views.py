from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Home
def index(request):
    context = {
        "title": "Welcome!",
        "header": "Welcome!"
    }
    return render(request,'users/index.html', context)


# Registers new users
def register(request):
    errors = User.objects.reg_validator(request.POST)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'register')
        return redirect('/')

    if errors.alias:
        request.session['name'] = errors.alias
    else:
        request.session['name'] = errors.name

    request.session['id'] = errors.id
    request.session['is_valid'] = True

    return redirect('/books')


# Logs the user in
def login(request):
    errors = User.objects.log_validator(request.POST)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'login')
        return redirect('/')

    if errors.alias:
        request.session['name'] = errors.alias
    else:
        request.session['name'] = errors.name

    request.session['id'] = errors.id
    request.session['is_valid'] = True

    return redirect('/books')


# Logs the user out
def logout(request):
    request.session.pop('id', None)
    request.session.pop('is_valid', None)

    return redirect('/')
