from email import message
from django.shortcuts import render
from django.contrib import messages
from .models import Contact


# Create your views here.

def basketball(request):
    return render(request, 'main/Basketball.html')


def gallery(request):
    return render(request, 'main/Gallery.html')


def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request, ('Message sent successfully!'))
        return render(request, 'main/Contact.html') 
    return render(request, 'main/Contact.html')


def explore(request):
    return render(request, 'main/explore.html')


def kids(request):
    return render(request, 'main/Kids.html')


def nba(request):
    return render(request, 'main/NBA.html')


def p404(request):
    return render(request, 'main/p404.html')


def rate(request):
    return render(request, 'main/Rate.html')


def sneakers(request):
    return render(request, 'main/Sneakers.html')


def women(request):
    return render(request, 'main/Women.html')


# def register(request):
#     return render(request, 'register/register.html')


# def thankcontact(request):
#     return render(request, 'main/thankcontact.html')
