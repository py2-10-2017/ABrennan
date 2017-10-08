from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^timedisplay/$', views.index),
    url(r'^time_display/$', views.index),
    url(r'^page/$', views.page)
]
