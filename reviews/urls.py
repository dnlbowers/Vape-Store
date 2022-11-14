from django.urls import path
from . import views

urlpatterns = [
    path(
        'create/<product_id>/',
        views.CreateReview.as_view(),
        name='add_review'),
    path(
        'product/<product_id>/edit-review/<review_id>/',
        views.EditReview.as_view(),
        name='edit_review'),
    path(
        'product/<product_id>/delete/<review_id>/',
        views.DeleteReview.as_view(),
        name='delete_review'),
]
