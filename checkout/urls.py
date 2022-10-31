from django.urls import path
from . import views

urlpatterns = [
    path('', views.Checkout.as_view(), name='checkout'),
]
