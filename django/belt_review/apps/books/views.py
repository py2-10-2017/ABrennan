from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.db.models import Count

# book home
def index(request):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    context = {
        "books": Review.objects.order_by("-created_at"),
        "title": 'Books Home',
    }
    return render(request,'books/books.html', context)

# display form to add book and review
def book_add(request):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    context = {
        "title": 'Add a New Book Title and Review',
        "authors": Author.objects.all(),
    }
    return render(request,'books/book_new.html', context)

# validates book form and adds to db
def book_create(request):
    u_id = request.session['id']
    errors = Book.objects.book_validator(request.POST, u_id)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'books')
        return redirect('/books/add')

    return redirect('/books/'+str(errors.id))

# displays a single book page
def book_page(request, book_id):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    context = {
        'book': Book.objects.get(id=book_id),
        "title": 'Add a New Book Title and Review',
    }
    return render(request, 'books/book.html', context)

# validates review form and adds to db
def review_add(request, book_id):
    u_id = request.session['id']
    errors = Book.objects.review_validator(request.POST, u_id, book_id)

    if type(errors) == list:
        for error in errors:
            messages.error(request, error, 'books')
        return redirect('/books/'+book_id)

    return redirect('/books/'+book_id)

# displays a single user page
def user_page(request, user_id):
    try:
        request.session['is_valid']
    except KeyError:
        return redirect('/')

    reviews = Book.objects.annotate(review_count=Count('reviews')).filter(reviews__user=user_id)
    user = Review.objects.filter(user_id=user_id)[0]

    context = {
        "reviews": reviews,
        "title": 'User Reviews',
        "count": len(reviews),
        "user": user
    }
    return render(request, 'books/user.html', context)

# deletes review posted by user
def review_delete(request, review_id):
    r = Review.objects.get(id=review_id)
    r.delete()

    return redirect('/books')
