from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.db.models import Count

# Home
def index(request):
    context = {
        "title": "Home Page",
        "header": "Welcome to the Test"
    }
    return render(request,'users/index.html', context)

# Page to register
def register(request):
    context = {
        "title": "Register",
    }
    return render(request,'users/register.html', context)


# Registers new users
def register_create(request):
    errors = User.objects.reg_validator(request.POST, 9)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'register')
        return redirect('/register')

    request.session['id'] = errors.id
    request.session['is_valid'] = True

    return redirect('/dashboard/admin')


# Page to login
def signin(request):
    context = {
        "title": "Signin",
    }
    return render(request,'users/signin.html', context)


# Logs the user in
def signin_success(request):
    errors = User.objects.log_validator(request.POST)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'login')
        return redirect('/signin')

    request.session['id'] = errors.id
    request.session['is_valid'] = True

    return redirect('/dashboard')


# User dashboard
def dash(request):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    l = User.objects.get(id=request.session['id']).level

    if l == 9:
        return redirect('/dashboard/admin')
    else:
        context = {
            "users": User.objects.all(),
            "title": "All Users",
        }
        return render(request,'users/dash_user.html', context)


# Admin dashboard
def dash_admin(request):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    l = User.objects.get(id=request.session['id']).level

    if l != 9:
        return redirect('/dashboard')
    else:
        context = {
            "users": User.objects.all(),
            "title": "Manage Users",
        }
        return render(request,'users/dash_admin.html', context)


# Page to add new user
def new(request):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    context = {
        "title": "Add a New User",
    }
    return render(request,'users/new.html', context)


# Registers new users
def user_create(request):
    errors = User.objects.reg_validator(request.POST, 1)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'register')
        return redirect('/users/new')

    return redirect('/dashboard/admin')


# Page to edit logged in user's profile
def edit(request):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    user = User.objects.get(id=request.session['id'])

    context = {
        "user": user,
        "title": "Edit Profile",
    }
    return render(request,'users/edit_self.html', context)


# Updates logged in user's contact
def self_contact(request):
    errors = User.objects.contact_validator(request.POST, request.session['id'])

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'contact')
        return redirect('/users/edit')

    return redirect('/dashboard')


# Updates logged in user's password
def self_pswd(request):
    errors = User.objects.pswd_validator(request.POST, request.session['id'])

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'pswd')
        return redirect('/users/edit')

    return redirect('/dashboard')


# Updates logged in user's description
def self_desc(request):
    errors = User.objects.desc_validator(request.POST, request.session['id'])

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'desc')
        return redirect('/users/edit')

    return redirect('/dashboard')


# Page to edit another user's profile
def user_edit(request, user_id):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    user = User.objects.get(id=user_id)

    context = {
        "user": user,
        "title": "Edit User #"+str(user_id),
    }
    return render(request,'users/edit_user.html', context)


# Updates another user's contact
def user_contact(request, user_id):
    errors = User.objects.contact_validator(request.POST, user_id)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'contact')
        return redirect('/users/edit/'+user_id)

    return redirect('/dashboard')


# Updates another user's password
def user_pswd(request, user_id):
    errors = User.objects.pswd_validator(request.POST, user_id)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'pswd')
        return redirect('/users/edit/'+user_id)

    return redirect('/dashboard')


# Deletes a user
def user_destroy(request, user_id):

    if str(request.session['id']) == user_id:
        messages.error(request, 'You cannot delete yourself', 'delete')
        return redirect('/dashboard/admin')
    else:
        u = User.objects.get(id=user_id)
        u.delete()

    return redirect('/dashboard/admin')



























# Logs the user out
def logout(request):
    request.session.pop('id', None)
    request.session.pop('is_valid', None)

    return redirect('/')
