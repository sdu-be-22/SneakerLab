from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'model', 'category')


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(JobVacancies)
admin.site.register(JobCategory)
