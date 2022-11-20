from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.ContactUs.as_view(),
        name='contact_us'),
]
