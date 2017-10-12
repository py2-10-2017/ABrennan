from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blogs$', views.index),
    url(r'^blogs/new/$', views.new),
    url(r'^blogs/create/$', views.create),
    url(r'^blogs/(?P<blog_id>[0-9]+)/$', views.show),
    url(r'^blogs/(?P<blog_id>[0-9]+)/edit/$', views.edit),
    url(r'^blogs/(?P<blog_id>[0-9]+)/delete/$', views.delete)
]
