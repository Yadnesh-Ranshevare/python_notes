from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstApp,name="first-app"),
    path('users', views.user, name="users"),
    path('users/<str:userName>/', views.userName, name="userName"),
    path('setCookie', views.setCookie, name="setCookie"),
]