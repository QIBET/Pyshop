from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product_api', views.ProductViewSet),
router.register(r'offer_api', views.OfferViewSet),



urlpatterns = [
    path('', views.index ),
    path('api_root', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]