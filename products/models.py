from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
    
    def save_product():
        return Product.save()

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_order = models.ForeignKey(Offer, on_delete= models.CASCADE, related_name='code')