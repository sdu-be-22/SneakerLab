from django.urls import path
from . import views

urlpatterns = [
    path('', views.basketball, name='home'),    
    path('store', views.sneakers, name='sneakers'),
    path('cart', views.cart, name='cart'),    
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('search/', views.search, name='search'),
]