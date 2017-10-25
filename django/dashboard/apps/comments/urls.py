from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/show/(?P<user_id>\d+)', views.user_show),
    url(r'^messages/(?P<user_id>\d+)/new', views.message),
    url(r'^comments/(?P<user_id>\d+)/new/(?P<msg_id>\d+)', views.comment),
]
