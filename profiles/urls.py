from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.Profile.as_view(),
        name='profile'),
    path(
        'completed_orders/<order_number>',
        views.CompletedOrders.as_view(),
        name='completed_orders'),
]
