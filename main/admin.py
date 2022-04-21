from django.contrib import admin

# Register your models here.
from .models import Contact, SneakerForMan, SneakerForWoman, SneakerForKid

admin.site.register(Contact)
admin.site.register(SneakerForMan)
admin.site.register(SneakerForWoman)
admin.site.register(SneakerForKid)