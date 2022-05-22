from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from main.forms import *
from .models import *
from django.http import JsonResponse
import json
from django.contrib import messages
import datetime
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

# Create your views here.

def basketball(request):
    context={}
    return render(request, 'main/Basketball.html', context)


def sneakers(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()

    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    sneakers = p.get_page(page)

    context={'products':products, 'cartItems':cartItems,'sneakers':sneakers}
    return render(request, 'main/Sneakers.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'main/Cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'main/Checkout.html', context)


def contact(request):
    if request.method=="POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactUsForm()
        context={'form':form}
        return render(request, 'main/Contact.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                zipcode = data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in...')
        
    return JsonResponse('Payment complete', safe=False)


def searchbymodel(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    if request.method == "POST":
        searched = request.POST['searched']
        sneakers = Product.objects.filter(model__contains=searched)

        p = Paginator(Product.objects.all(), 6)
        page = request.GET.get('page')
        sneakerss = p.get_page(page)
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})

    else:
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})



def searchbybrand(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    if request.method == "POST":
        searched = request.POST['searched']
        sneakers = Product.objects.filter(name__contains=searched)

        p = Paginator(Product.objects.all(), 6)
        page = request.GET.get('page')
        sneakerss = p.get_page(page)
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})

    else:
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})



def searchbycategory(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    if request.method == "POST":
        searched = request.POST['searched']
        sneakers = Product.objects.filter(category__contains=searched)

        p = Paginator(products, 6)
        page = request.GET.get('page')
        sneakerss = p.get_page(page)
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})

    else:
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})



def jobvacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VacancyForm()
    return render(request, 'main/Job.html', {'form': form})



class RegisterUser(CreateView):
    form_class = RegisterForm 
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')

