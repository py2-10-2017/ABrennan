from django.shortcuts import render, HttpResponse, redirect

# blog home
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

# new blog form
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

# create new blog
def create(request):
    return redirect ('/')

# display blog
def show(request, blog_id):
    response = "placeholder to display blog " + blog_id
    return HttpResponse(response)

# edit blog
def edit(request, blog_id):
    response = "placeholder to edit blog " + blog_id
    return HttpResponse(response)

# display blog
def delete(request, blog_id):
    response = "placeholder to delete blog " + blog_id
    return HttpResponse(response)
