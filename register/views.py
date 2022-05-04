from cmath import log
import imp
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return render(response, "main/Basketball.html")

        else:
            return render(response, "register/register.html", {"form":form})

        
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main/Basketball.html')
        else:
            messages.info(request, 'Username or password is incorrect')

    
    return render(request, "register/login.html", {"form":form})