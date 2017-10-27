from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^notes/new$', views.note_new),
    url(r'^notes/delete/(?P<note_id>\d+)$', views.note_delete),
    url(r'^notes/edit/(?P<note_id>\d+)$', views.note_edit),
    url(r'^notes', views.index),
]
