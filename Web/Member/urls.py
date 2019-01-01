from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
	path('logout/', views.logout,name='logout'),
	path('sign_up/', views.sign_up,name='sign_up'),
	path('modify/',views.modify,name='modify'),
	path('index/', views.index,name='index'),
	path('playmode/',views.playmode,name = 'playmode'),
	path('playmode=<int:pm>/',views.playmode,name = 'playmode'),
	path('Table/',views.tableinformation,name = 'table'),
	path('Table/<int:tid>',views.tableinformation,name = 'table'),
	path('connect/',views.connect,name='connect'),
#	path('GameStart/',views.GameStart,name = 'GameStart')
	#path('modify_password/',views.modify_password),
]