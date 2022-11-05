from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from django.conf import settings

from shopping_cart.contexts import cart_contents
from .forms import PaymentForm

import stripe
import json


class Checkout(View):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    payment_form = PaymentForm()
    template = 'checkout/checkout.html'
    cart = {}

    def get(self, request, *args, **kwargs):
        self.cart = request.session.get('cart', {})
        if not self.cart:
            messages.error(request, "Your cart is currently empty")
            return redirect(reverse('products'))

        to_be_charged = round(cart_contents(request)['grand_total']*100)

        stripe.api_key = self.stripe_secret_key

        payment_intent = stripe.PaymentIntent.create(
            amount=to_be_charged,
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            'payment_form': self.payment_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': payment_intent.client_secret,
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        self.cart = request.session.get('cart', {})
        if not self.cart:
            messages.error(request, "Your cart is currently empty")
            return redirect(reverse('products'))

        to_be_charged = round(cart_contents(request)['grand_total']*100)

        stripe.api_key = self.stripe_secret_key

        payment_intent = stripe.PaymentIntent.create(
            amount=to_be_charged,
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            'payment_form': self.payment_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': payment_intent.client_secret,
            'to_be_charged': to_be_charged,
        }
        return render(request, self.template, context)
