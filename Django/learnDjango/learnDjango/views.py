from django.http import  HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, World! This is my first Django app.")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def template(request):
    return render(request, 'index.html')

def useLayout(request):
    return render(request, 'useLayout.html')
