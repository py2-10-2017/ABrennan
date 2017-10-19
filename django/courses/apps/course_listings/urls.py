from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/create', views.create),
    url(r'^courses/(?P<course_id>\d+)/delete', views.delete),
    url(r'^courses/(?P<course_id>\d+)/destroy', views.destroy),
    url(r'^courses/(?P<course_id>\d+)/comments/create', views.create_comment),
    url(r'^courses/(?P<course_id>\d+)/comments/new', views.new_comment),
    url(r'^courses/(?P<course_id>\d+)/comments', views.comments),
]
