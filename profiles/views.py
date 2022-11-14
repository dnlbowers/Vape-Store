from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


class Profile(LoginRequiredMixin, View):

    login_url = '/accounts/login/'

    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:

            messages.error(
                self.request,
                'You need to be logged in to view your profile')

        else:

            profile = get_object_or_404(UserProfile, user=self.request.user)
            form = UserProfileForm(instance=profile)
            completed_orders = profile.orders.all()

            context = {
                'details_form': form,
                'completed_orders': completed_orders,
                'on_profile_page': True,
            }

            return render(self.request, 'profiles/profile.html', context)

    def post(self, *args, **kwargs):

        if not self.request.user.is_authenticated:

            messages.error(
                self.request,
                'You need to be logged in to update your profile')

        else:

            profile = get_object_or_404(UserProfile, user=self.request.user)
            form = UserProfileForm(self.request.POST, instance=profile)
            completed_orders = profile.orders.all()

            if form.is_valid():

                form.save()
                messages.success(self.request, 'Profile updated successfully')
                return redirect(reverse('profile'))

            else:
                messages.error(
                    self.request,
                    'Update failed. Please try again.')
                context = {
                    'details_form': form,
                    'completed_orders': completed_orders,
                    'on_profile_page': True,
                }

                return render(self.request, 'profiles/profile.html', context)


class CompletedOrders(View):

    def get(self, *args, **kwargs):
        order_number = self.kwargs.get('order_number')
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(
            self.request,
            f'This is a past confirmation for order no. {order_number}.'
            'A confirmation email was sent at the time of purchase.')

        template = 'checkout/checkout-success.html'
        context = {
            'order': order,
            'from_profile': True
        }

        return render(self.request, template, context)
