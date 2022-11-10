from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile.as_view(), name='profile'),
]
