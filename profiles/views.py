from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


class Profile(View):

    def get(self, *args, **kwargs):

        profile = get_object_or_404(UserProfile, user=self.request.user)
        form = UserProfileForm(instance=profile)
        completed_orders = profile.orders.all()

        context = {
            'form': form,
            'completed_orders': completed_orders,
            'on_profile_page': True,
        }

        return render(self.request, 'profiles/profile.html', context)

    def post(self, *args, **kwargs):

        profile = get_object_or_404(UserProfile, user=self.request.user)
        form = UserProfileForm(self.request.POST, instance=profile)
        completed_orders = profile.orders.all()

        if form.is_valid():

            form.save()
            messages.success(self.request, 'Profile updated successfully')
            return redirect(reverse('profile'))

        else:
            messages.error(self.request, 'Update failed. Please try again.')
            context = {
                'form': form,
                'completed_orders': completed_orders,
                'on_profile_page': True,
            }

            return render(self.request, 'profiles/profile.html', context)
