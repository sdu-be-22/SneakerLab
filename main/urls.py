from django.urls import path

from register.forms import RegisterForm
from . import views

urlpatterns = [
    path('', views.basketball, name='home'),    
    path('store', views.sneakers, name='sneakers'),
    path('cart', views.cart, name='cart'),    
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('searchbymodel/', views.searchbymodel, name='searchbymodel'),
    path('searchbybrand/', views.searchbybrand, name='searchbybrand'),
    path('searchbycategory/', views.searchbycategory, name='searchbycategory'),
    path('jobvacancy/', views.jobvacancy, name='jobvacancy'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]
