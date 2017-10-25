from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/admin', views.dash_admin),
    url(r'^dashboard', views.dash),
    url(r'^register/create', views.register_create),
    url(r'^register', views.register),
    url(r'^users/edit/(?P<user_id>\d+)/delete', views.user_destroy),
    url(r'^users/edit/(?P<user_id>\d+)/contact', views.user_contact),
    url(r'^users/edit/(?P<user_id>\d+)/pswd', views.user_pswd),
    url(r'^users/edit/(?P<user_id>\d+)', views.user_edit),
    url(r'^users/edit/contact', views.self_contact),
    url(r'^users/edit/pswd', views.self_pswd),
    url(r'^users/edit/desc', views.self_desc),
    url(r'^users/edit', views.edit),
    url(r'^users/create', views.user_create),
    url(r'^users/new', views.new),
    url(r'^signin/success', views.signin_success),
    url(r'^signin', views.signin),
    url(r'^logout', views.logout),
    url(r'^$', views.index)
]
