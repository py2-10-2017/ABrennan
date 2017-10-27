from django.shortcuts import render, HttpResponse
from models import *


# Home
def index(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

# Partial - posts
def posts(request):
    p = Post.objects.create(post=request.POST['post'])
    context = {
        "post": p
    }
    return render(request, 'posts/posts.html', context)
