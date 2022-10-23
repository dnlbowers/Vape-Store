from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewShoppingCart.as_view(), name='view_cart'),
    path('add/<product_id>/', views.AddToCart.as_view(), name='add_to_cart'),
]
