# hrmgmt/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    # /hr/
    url(r'^$', views.index, name='index')
]


