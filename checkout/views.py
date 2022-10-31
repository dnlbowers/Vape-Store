from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages

from .forms import PaymentForm


class Checkout(View):

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
