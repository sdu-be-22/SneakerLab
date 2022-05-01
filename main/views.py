from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.contrib import messages
import datetime
from django.core.paginator import Paginator

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
    context={}
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


def search(request):
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

        p = Paginator(products, 6)
        page = request.GET.get('page')
        sneakerss = p.get_page(page)
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})

    else:
        return render(request, 'main/search.html', {'products':products, 'cartItems':cartItems,'searched':searched , 'sneakers':sneakers, 'sneakerss':sneakerss})