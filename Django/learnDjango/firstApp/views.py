from django.shortcuts import render
from .models import UserModel 
from django.shortcuts import get_object_or_404

# Create your views here.
def firstApp(request):
    return render(request, 'firstApp/firstApp.html')

def user(request):
    user = UserModel.objects.all()
    return render(request, 'firstApp/user.html', {'users': user})

def userName(request,userName):
    user = get_object_or_404(UserModel, name=userName)
    return render(request, 'firstApp/userName.html', {'user': user})
    

