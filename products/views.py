
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Offer
from .serializers import ProductSerializer, OfferSerializer

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer