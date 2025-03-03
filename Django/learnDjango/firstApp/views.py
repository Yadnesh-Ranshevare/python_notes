from django.shortcuts import render
from .models import UserModel 
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def firstApp(request):
    return render(request, 'firstApp/firstApp.html')

def user(request):
    user = UserModel.objects.all()
    return render(request, 'firstApp/user.html', {'users': user})

def userName(request,userName):
    user = get_object_or_404(UserModel, name=userName)
    return render(request, 'firstApp/userName.html', {'user': user})
@csrf_exempt
def setCookie(request):
    response = render(request, 'firstApp/firstApp.html')
    response.set_cookie('dj4e_cookie', 'value', max_age=1000)
    return response
    

