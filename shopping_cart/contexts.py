from decimal import Decimal
from django.views import View
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import AllProducts


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    if total < settings.FREE_SHIPPING_QUALIFIER:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_QUALIFIER - total
    else:
        shipping = 0
        free_shipping_delta = 0

        # cart_total = shipping + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_qualifier': settings.FREE_SHIPPING_QUALIFIER,
        # 'cart_total': cart_total,

    }

    return context
