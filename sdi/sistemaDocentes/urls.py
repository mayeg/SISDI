from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [

    path('login', views.LoginView.as_view(), name='login'),
    path('index', views.IndexView.as_view(), name='index'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('docente-list', views.DocenteListViews.as_view(), name='docente-list'),
]
