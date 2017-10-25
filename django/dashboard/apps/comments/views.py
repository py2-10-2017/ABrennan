from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Page to show user information
def user_show(request, user_id):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    user = User.objects.get(id=user_id)
    msgs = Message.objects.filter(user_id=user_id)
    comments = Comment.objects.filter(user_id=user_id)

    context = {
        "user": user,
        "msgs": msgs,
        "comments": comments,
        "title": "User Information",
    }
    return render(request,'comments/show.html', context)

# Messages
def message(request, user_id):
    commenter = request.session['id']
    errors = Message.objects.message_validator(request.POST, user_id, commenter)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'message')

    return redirect('/users/show/'+user_id)

# Comments
def comment(request, user_id, msg_id):
    commenter = request.session['id']
    errors = Comment.objects.comment_validator(request.POST, user_id, commenter, msg_id)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'message')

    return redirect('/users/show/'+user_id)
