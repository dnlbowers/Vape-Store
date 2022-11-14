from django.urls import path
from . import views

urlpatterns = [
    path(
        'create/<product_id>/',
        views.CreateReview.as_view(),
        name='add_review'),
    path(
        'edit/<int:pk>/',
        views.EditReview.as_view(),
        name='edit_review'),
]
