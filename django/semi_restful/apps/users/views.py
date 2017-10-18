from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# home
def index(request):

    return redirect('/users')

# a GET request to /users - calls the index method to display all the users. This will need a template.
def users(request):

    context = {
        "users": User.objects.all(),
        "page_title": 'All Users'
    }
    return render(request,'users/users.html', context)


def user(request, user_id):

    context = {
        "user": User.objects.get(id=user_id),
        "page_title": 'User Data'
    }
    return render(request,'users/user.html', context)


# GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
def new(request):

    context = {
        "page_title": 'New User'
    }
    return render(request, 'users/new.html', context)


# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
def edit(request, user_id):

    context = {
        "user": User.objects.get(id=user_id),
        "page_title": 'Update User'
    }
    return render(request, 'users/edit.html', context)


# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
def create(request):

    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    elif User.objects.filter(email=request.POST['email']):
        messages.add_message(request, messages.INFO, "This email is already taken")
        return redirect('/users/new')
    else:
        u = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        u.save()
        messages.add_message(request, messages.INFO, "The user has been added")
        return redirect('/users')


# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
def delete(request, user_id):

    u = User.objects.get(id=user_id)
    u.delete()

    messages.add_message(request, messages.INFO, "The user has been deleted")
    return redirect('/users')


# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
def update(request, user_id):

    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+user_id+'/edit')
    elif len(User.objects.filter(email=request.POST['email'])) > 1:
        messages.add_message(request, messages.INFO, "This email is already taken")
        return redirect('/users/'+user_id+'/edit')
    else:
        u = User.objects.get(id=user_id)
        u.first_name = request.POST['first_name']
        u.last_name = request.POST['last_name']
        u.email = request.POST['email']
        u.save()
        messages.add_message(request, messages.INFO, "The user has been updated")
        return redirect('/users/'+user_id)
