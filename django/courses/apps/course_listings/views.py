from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# home
def index(request):

    context = {
        "courses": Course.objects.all(),
        "descs": Desc.objects.all(),
        "page_title": 'All Courses'
    }

    return render(request,'course_listings/courses.html', context)


def create(request):

    error1 = Course.objects.basic_validator(request.POST)
    error2 = Desc.objects.basic_validator(request.POST)

    if len(error1):
        for tag, error in error1.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    elif len(error2):
        for tag, error in error2.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        n = request.POST['name']
        d = request.POST['desc']
        Course.objects.create(name=n)

        x = Course.objects.filter(name=n)
        Desc.objects.create(desc=d, course=Course.objects.get(id=x[0].id))

        messages.add_message(request, messages.INFO, "The course has been added")
        return redirect('/')


def destroy(request, course_id):

    c = Course.objects.get(id=course_id)
    c.delete()

    messages.add_message(request, messages.INFO, "The course has been deleted")
    return redirect('/')


def delete(request, course_id):

    context = {
        "course": Course.objects.get(id=course_id),
        "descs": Desc.objects.filter(course_id=course_id),
        "page_title": 'Delete Course'
    }

    return render(request,'course_listings/delete.html', context)


def comments(request, course_id):

    context = {
        "course": Course.objects.get(id=course_id),
        "descs": Desc.objects.filter(course_id=course_id),
        "comments": Comment.objects.filter(course_id=course_id),
        "page_title": 'Comments for Course #'+course_id
    }

    return render(request,'course_listings/comments.html', context)


def new_comment(request, course_id):

    context = {
        "course": Course.objects.get(id=course_id),
        "descs": Desc.objects.filter(course_id=course_id),
        "comments": Comment.objects.filter(course_id=course_id),
        "page_title": 'Add a Comment'
    }

    return render(request,'course_listings/comment.html', context)



def create_comment(request, course_id):

    error3 = Comment.objects.basic_validator(request.POST)

    if len(error3):
        for tag, error in error3.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses/'+course_id+'/comments/new')
    else:
        c = request.POST['comment']

        Comment.objects.create(comment=c, course_id=course_id)

        messages.add_message(request, messages.INFO, "The comment has been added")
        return redirect('/courses/'+course_id+'/comments')
