from django.shortcuts import render, HttpResponse, redirect

# surveys home
def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

# new survey
def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)
