from email.policy import HTTP
import http
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def newproduct(request):
    return HttpResponse('this is new product')

def return_time(request):
    date = datetime.now()
    message = 'server is live now, current time is'
    return Response(data=message + date, status=status.HTTP_200_OK)