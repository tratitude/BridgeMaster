from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.login,name='login'),
    path('login/', views.login,name='login'),
	path('logout/', views.logout,name='logout'),
	path('sign_up/', views.sign_up,name='sign_up'),
	path('modify/',views.modify,name='modify'),
	path('modify2/',views.modify2,name='modify2'),
	path('index/', views.index,name='index'),
	path('playmode/',views.playmode,name = 'playmode'),
	path('playmode=<int:pm>/',views.playmode,name = 'playmode'),
	path('Table/',views.tableinformation,name = 'table'),
	path('Table/<int:tid>',views.tableinformation,name = 'table'),
	path('Json/',views.Json,name='Json'),
	path('State/',views.State,name='State'),
	path('Administrator/',views.Administrator,name = 'Administrator'),
	path('Administrator/usermodify/<int:uid>/',views.usermodify,name='usermodify'),
	path('Administrator/userdelete/<int:uid>/',views.userdelete,name='userdelete'),
	path('data_fresh/',views.data_fresh,name='data_fresh'),
	path('Classic/',views.Classic,name='Classic'),
#	path('GameStart/',views.GameStart,name = 'GameStart')
#	path('modify_password/',views.modify_password),
]