from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductsView.as_view(), name='products'),
]
