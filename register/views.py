import imp
from django.shortcuts import render, redirect
from .forms import RegisterForm

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