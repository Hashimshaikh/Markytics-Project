from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    path('login_out', views.login_out, name="login_out"),
    path('incidents', views.incidents, name="incidents"),
    path('register', views.register, name="register"),
    #path('profile', views.profile, name="profile")
    #path('', include("django.contrib.auth.urls")),
]
