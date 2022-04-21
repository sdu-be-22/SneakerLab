from email import message
from django.shortcuts import render
from django.contrib import messages
from .models import Contact, SneakerForKid, SneakerForMan, SneakerForWoman
# from .forms import ProductCategoriesForm


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



def nba(request):
    return render(request, 'main/NBA.html')


def p404(request):
    return render(request, 'main/p404.html')


def rate(request):
    return render(request, 'main/Rate.html')


def sneakers(request):
    all_sneakers = SneakerForMan.objects.all
    return render(request, 'main/Sneakers.html', {'all':all_sneakers})


def women(request):
    all_sneakers = SneakerForWoman.objects.all
    return render(request, 'main/Women.html', {'all':all_sneakers})


def kids(request):
    all_sneakers = SneakerForKid.objects.all
    return render(request, 'main/Kids.html', {'all':all_sneakers})

def collabformen(request):
    all_sneakers = SneakerForMan.objects.all
    return render(request, 'main/collabformen.html', {'all':all_sneakers})


def collabforwomen(request):
    all_sneakers = SneakerForWoman.objects.all
    return render(request, 'main/collabformen.html', {'all':all_sneakers})


def collabforkid(request):
    all_sneakers = SneakerForKid.objects.all
    return render(request, 'main/collabformen.html', {'all':all_sneakers})


def searchsneakerformen(request):
    if request.method == "POST":
        searched = request.POST['searched']
        sneakers = SneakerForMan.objects.filter(sneaker_model__contains=searched)
        return render(request, 'main/search.html', {'searched':searched , 'sneakers':sneakers})

    else:
        return render(request, 'main/search.html', {})

# def productcategory(request):
#     form = ProductCategoriesForm()
# def register(request):
#     return render(request, 'register/register.html')


# def thankcontact(request):
#     return render(request, 'main/thankcontact.html')
