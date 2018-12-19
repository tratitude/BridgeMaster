from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
	path('logout/', views.logout,name='logout'),
	path('index/', views.index,name='index'),
	path('sign_up/', views.sign_up,name='sign_up'),
	path('modify/',views.modify,name='modify'),
	#path('modify_password/',views.modify_password),
]