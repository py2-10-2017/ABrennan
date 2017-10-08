from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.utils import timezone

def index(request):
    time = {
        'now': timezone.localtime(timezone.now())
    }
    return render(request,'timedisplay/index.html', time)

def page(request):
    context = {
        "somekey":"somevalue"
    }
    return render(request,'timedisplay/page.html', context)
