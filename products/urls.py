from django.urls import path
from . import views



urlpatterns = [
    path('', views.index ),
    path('new', views.newproduct),
    path('timer/', views.return_time, name='timer')
]