from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewShoppingCart.as_view(), name='view_cart'),
]
