from django.shortcuts import (render,
                              redirect, reverse, get_object_or_404,
                              HttpResponse)
from django.views import View
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from shopping_cart.contexts import cart_contents
from .forms import PaymentForm
from .models import Order, OrderLineItem
from products.models import AllProducts
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    A view that takes in the checkout data and
    stores it in the user's session
    """

    try:

        payment_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(payment_id, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


class Checkout(View):
    """
    A view that renders the checkout page and gets the
    payment form data from the profile if one is present
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    template = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        """
        Handles the GET request for the checkout page
        and renders the form with any previous information prefilled.

        """

        cart = request.session.get('cart', {})

        if not cart:

            messages.error(request, "Your cart is currently empty")

            return redirect(reverse('products'))

        charge_amount = round(cart_contents(request)['grand_total'] * 100)

        stripe.api_key = self.stripe_secret_key

        payment_intent = stripe.PaymentIntent.create(

            amount=charge_amount,
            currency=settings.STRIPE_CURRENCY,

        )

        if request.user.is_authenticated:

            try:
                profile = UserProfile.objects.get(user=request.user)

                payment_form = PaymentForm(initial={
                    'full_name': profile.default_delivery_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })

            except UserProfile.DoesNotExist:

                payment_form = PaymentForm()
        else:

            payment_form = PaymentForm()

        context = {
            'payment_form': payment_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': payment_intent.client_secret,
            'charge_amount': charge_amount,
        }

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request for the checkout page
        and processes the form data, creates the order
        and adjusts the stock level
        """

        cart = request.session.get('cart', {})

        shipping_details = {

            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number'],
        }

        payment_form = PaymentForm(shipping_details)

        if payment_form.is_valid():

            order = payment_form.save(commit=False)
            payment_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_payment_id = payment_id
            order.original_cart = json.dumps(cart)
            order.save()

            for product_id, product_details in cart.items():

                try:
                    product = AllProducts.objects.get(id=product_id)

                    # reduces the stock level by the quantity ordered
                    if product.stock_level > 0:

                        product.stock_level -= product_details
                        product.save()

                    else:

                        messages.error(request, (
                            "Sorry, we are currently out of stock of {0}."
                            "Please remove this item from your cart and try "
                            "again later.").format(product.name))

                        order.delete()
                        return redirect(reverse('view_cart'))

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=product_details,
                    )
                    order_line_item.save()

                except AllProducts.DoesNotExist:

                    messages.error(request, (
                        "One of your products seems to no longer exist \
                            in our system."
                        "Please reach out to us for assistance")
                    )

                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse(
                'checkout_success',
                args=[order.order_number]
            ))

        else:

            messages.error(request, "Unable to process your order. \
                Please check the details you have entered before \
                   resubmitting the order")


class CheckoutSuccess(View):
    """
    A view that renders the checkout success page
    and saves shipping details to the profile if the
    user ticks the save info box
    """

    template = 'checkout/checkout-success.html'

    def get(self, request, order_number, *args, **kwargs):

        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)
        order.times_viewed += 1
        order.save()

        if request.user.is_authenticated:

            profile = UserProfile.objects.get(user=request.user)

            # Attach the user's profile to the order
            order.user_profile = profile
            order.save()

            # Save the user's info
            if save_info:

                profile_data = {

                    'default_delivery_name': order.full_name,
                    'default_phone_number': order.phone_number,
                    'default_country': order.country,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_county': order.county,

                }

                user_profile_form = UserProfileForm(
                    profile_data, instance=profile)

                if user_profile_form.is_valid():

                    user_profile_form.save()
        if order.times_viewed > 1:

            messages.warning(
                request, f'Our sincere apologies however this\
                 page cannot be revisited. If you need to view your order\
                     again please use the order history page.\n'
                'If you were not signed in when you placed your order\
                            kindly contact us via the "contact us" page\
                                and we will be happy to assist you.')

            return redirect(reverse('home'))
        else:

            messages.success(
                request,
                f'We\'ve successfully received your order. Your order \
                    reference number is {order_number}, and a confirmation \
                        email will be sent to {order.email} shortly. Any \
                            questions can be directed to our customer service \
                                team via the "contact us" page.')

            if 'cart' in request.session:

                del request.session['cart']

            context = {
                'order': order,
            }

            return render(request, self.template, context)
