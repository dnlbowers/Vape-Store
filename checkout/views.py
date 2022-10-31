from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages

from .forms import OrderForm


class Checkout(View):

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is currently empty")
            return redirect(reverse('products'))
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
        }
        return render(request, template, context)
