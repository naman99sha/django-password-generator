from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
   
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length=int(request.GET.get('length'))
    password=''
    for x in range(length):
        password += random.choice(characters)
    return render(request,'generator/password.html',{'password':password})

def about(request):
    return render(request, 'generator/about.html')

# Create your views here.
