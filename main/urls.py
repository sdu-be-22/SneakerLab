from django.urls import path
from . import views

urlpatterns = [
    path('', views.basketball, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('explore', views.explore, name='explore'),
    path('kids', views.kids, name='kids'),
    path('nba', views.nba, name='nba'),
    path('p404', views.p404, name='p404'),
    path('rate', views.rate, name='rate'),
    path('sneakers', views.sneakers, name='sneakers'),
    path('women', views.women, name='women'),
    # path('register', views.register, name='register'),
]
