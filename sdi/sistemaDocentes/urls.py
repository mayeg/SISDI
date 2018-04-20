from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    #url(r'^$', views.IndexView.as_view(), name="index"),
    path('login', views.LoginView.as_view(), name='login'),
    #url(r'^logout/$', views.LogoutView.as_view(), name="logout"),

]
