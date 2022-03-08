
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083,null=True)

    def __str__(self):
        return self.name
    
    def save_product(self):
        self.save()

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.code

    def save_offer(self):
        self.save()

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    product_bought = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bought', null=True)
    product_offer =  models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offered', null=True)

    def __str__(self):
        return self.customer_name

    def save_customer(self):
        self.save()
    
    def delete_customer(self):
        self.save_customer()
        self.delete()