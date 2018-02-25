from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^new$', views.new),
    url(r'^add_new$', views.add_new),
    url(r'^item/(?P<id>\d+)$', views.item),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit$', views.success),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),

]