from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.models import  User
from django.urls import reverse_lazy
from .models import Signup

# Create your views here.
def sign(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        data = Signup(username=uname, Email=email, phone=phone, password=password)
        data.save()
        return redirect('/login')

    return render(request,'pages/signUp.html')


def log(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        aaa=request.POST.get('password')
        return redirect('/index')

    return render(request,'pages/login.html')

def index(request):

    return render(request,'pages/index.html')