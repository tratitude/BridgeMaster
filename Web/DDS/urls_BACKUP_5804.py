from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.dds,name='dds')
=======

from . import views

urlpatterns = [
    path('', views.login,name='dds'),
>>>>>>> gitignore
]