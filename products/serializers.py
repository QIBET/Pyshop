from rest_framework import serializers
from .models import Product, Offer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'image_url')

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ('code', 'description', 'discount')
