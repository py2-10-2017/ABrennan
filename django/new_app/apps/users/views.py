from django.shortcuts import render, HttpResponse, redirect

# users home
def index(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

# register
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

# login
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)
