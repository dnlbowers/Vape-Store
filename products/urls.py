from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.AllProductsView.as_view(),
        name='products'
    ),
    path(
        '<slug:slug>/',
        views.ProductDetails.as_view(),
        name='product_detail'
    ),
    path(
        'edit/<slug:slug>/',
        views.EditExistingProduct.as_view(),
        name='edit_product'
    ),
    path(
        'delete/<int:product_id>/',
        views.DeleteProduct.as_view(),
        name='delete_product'
    ),
]
