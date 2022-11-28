from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


class Profile(LoginRequiredMixin, View):
    """
    A view to return the user's profile
    LoginRequiredMixin ensures that only logged
    in users can access this view
    """

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
                'profile': profile,
                'details_form': form,
                'completed_orders': completed_orders,
                'on_profile_page': True,
            }

            return render(self.request, 'profiles/profile.html', context)

    def post(self, *args, **kwargs):
        """
        Handles the form submission to update the users delivery details
        """

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
    """
    A view to return the user's completed orders
    from past check successes.
    """

    def get(self, *args, **kwargs):

        order_number = self.kwargs.get('order_number')
        order = get_object_or_404(Order, order_number=order_number)

        if self.request.user.id == order.user_profile.user.id:
            messages.info(
                self.request,
                f'This is a past confirmation for order no. {order_number}.'
                f'A confirmation email was sent to {order.email} at the time\
                     of purchase.')

            template = 'checkout/checkout-success.html'

            context = {
                'order': order,
                'from_profile': True
            }

            return render(self.request, template, context)

        else:

            messages.error(
                self.request,
                'Sorry, this order does not belong to you or\
                    you were not logged in at the time of purchase. \
                        Please contact us for assistance.')
            return redirect(reverse('home'))
