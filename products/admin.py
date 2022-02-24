from django.contrib import admin
from .models import Customer, Offer, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'location')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Customer, CustomerAdmin)
