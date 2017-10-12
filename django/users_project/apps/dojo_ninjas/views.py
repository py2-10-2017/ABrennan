from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder text for dojo ninjas"
    return HttpResponse(response)
