from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from django.conf import settings

from .forms import PaymentForm

import stripe
import json


class Checkout(View):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is currently empty")
            return redirect(reverse('products'))
        payment_form = PaymentForm()
        template = 'checkout/checkout.html'
        context = {
            'payment_form': payment_form,
        }
        return render(request, template, context)
