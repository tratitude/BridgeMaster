from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
	#path('logout/', views.logout),
	path('index/', views.index,name='index'),
	#path('sign/', views.sign),
	#path('modify/',views.modify),
	#path('modify_password/',views.modify_password),
]