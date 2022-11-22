from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import AllProducts


def cart_contents(request):

    cart_contents = []
    cart_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_id, quantity in cart.items():

        product = get_object_or_404(AllProducts, pk=product_id)
        cart_total += quantity * product.price
        product_count += quantity
        cart_contents.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product
        })

    if cart_total < settings.FREE_SHIPPING_QUALIFIER:

        shipping = cart_total * \
            Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        if shipping < settings.STANDARD_SHIPPING_MINIMUM:
            shipping = Decimal(settings.STANDARD_SHIPPING_MINIMUM)
        free_shipping_delta = settings.FREE_SHIPPING_QUALIFIER - cart_total

    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + cart_total

    context = {

        'cart_contents': cart_contents,
        'cart_total': cart_total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_qualifier': settings.FREE_SHIPPING_QUALIFIER,
        'grand_total': grand_total,

    }

    return context
