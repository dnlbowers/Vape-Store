from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from .models import UserProfile


class Profile(View):

    def get(self, *args, **kwargs):
        profile = get_object_or_404(UserProfile, user=self.request.user)
        context = {
            'profile': profile,
        }
        return render(self.request, 'profiles/profile.html', context)