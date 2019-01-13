from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dds,name='dds')
]
