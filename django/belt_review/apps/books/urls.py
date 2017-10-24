from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/(?P<user_id>\d+)', views.user_page),
    url(r'^reviews/(?P<review_id>\d+)/delete', views.review_delete),
    url(r'^books/(?P<book_id>\d+)/review', views.review_add),
    url(r'^books/(?P<book_id>\d+)', views.book_page),
    url(r'^books/create', views.book_create),
    url(r'^books/add', views.book_add),
    url(r'^books', views.index),
]
