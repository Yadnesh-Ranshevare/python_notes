from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstApp,name="first-app"),
]