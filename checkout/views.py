from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views import View
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from shopping_cart.contexts import cart_contents
from .forms import PaymentForm
from .models import Order, OrderLineItem
from products.models import AllProducts

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


class Checkout(View):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    template = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
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

        payment_form = PaymentForm()

        context = {
            'payment_form': payment_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': payment_intent.client_secret,
            'charge_amount': charge_amount,
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
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
            order = payment_form.save()

            for product_id, product_details in cart.items():
                try:
                    product = AllProducts.objects.get(id=product_id)

                    # start of stock management, need to add similiar to update line item model method
                    # product.stock_level -= product_details
                    # product.save()
                    # end of stock management

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

            return redirect(reverse(
                'checkout_success',
                args=[order.order_number]
            ))
        else:
            messages.error(request, "Unable to process your order. \
                Please check the details you have entered before \
                   resubmitting the order")


class CheckoutSuccess(View):

    template = 'checkout/checkout_success.html'

    def get(self, request, order_number, *args, **kwargs):
        order = get_object_or_404(Order, order_number=order_number)

        messages.success(request, f"We've successfully received your order. \
            Your order reference number is {order_number}, and a confirmation \
                email will be sent to {order.email} shortly. Any questions \
                    can be directed to our customer service team via the \
                        contact page.")

        if 'cart' in request.session:
            del request.session['cart']

        context = {
            'order': order,
        }

        return render(request, self.template, context)
