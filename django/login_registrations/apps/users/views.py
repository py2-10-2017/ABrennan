from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Home
def index(request):
    context = {
        "page_title": 'Registration'
    }
    return render(request,'users/index.html', context)


# Welcome screen after logging in
def success(request):
    context = {
        "page_title": 'Logged In'
    }
    return render(request,'users/success.html', context)


# Registers new users
def register(request):

    reg_errors = User.objects.reg_validator(request.POST)
    u = User.objects.filter(email=request.POST['r_email'])

    if len(reg_errors):
        for tag, error in reg_errors.iteritems():
            messages.error(request, error, extra_tags="register")
        return redirect('/')
    elif len(u):
        reg_errors["login"] = "Email is already taken"
        for tag, error in reg_errors.iteritems():
            messages.error(request, error, extra_tags="register")
        return redirect('/')
    else:
        pswd = bcrypt.hashpw(request.POST['r_password'].encode(), bcrypt.gensalt())
        u = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['r_email'], password=pswd)
        u.save()

        request.session['name'] = request.POST['first_name']

        return redirect('/success')

# Logs the user in
def login(request):

    log_errors = User.objects.log_validator(request.POST)
    u = User.objects.filter(email=request.POST['username'])
    pswd = request.POST['password']
    hashed = u[0].password.encode("utf-8")

    if len(log_errors):
        for tag, error in log_errors.iteritems():
            messages.error(request, error, extra_tags="login")
        return redirect('/')
    elif not len(u):
        log_errors["login"] = "That email does not exist"
        for tag, error in log_errors.iteritems():
            messages.error(request, error, extra_tags="login")
        return redirect('/')
    elif not bcrypt.checkpw(pswd.encode(), hashed):
        log_errors["password"] = "Invalid username/password"
        for tag, error in log_errors.iteritems():
            messages.error(request, error, extra_tags="login")
        return redirect('/')
    else:
        request.session['name'] = u[0].first_name

        return redirect('/success')


# Logs the user out
def logout(request):

    del request.session['name']

    return redirect('/')
