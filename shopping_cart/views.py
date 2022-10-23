from django.views.generic.base import TemplateView
from django.views import View  # noqa
from django.shortcuts import redirect


class ViewShoppingCart(TemplateView):
    """"
    View to render the shopping cart contents
    """
    template_name = 'shopping_cart/cart.html'


class AddToCart(View):
    """"
    View to add a quantity of a product to the shopping cart
    """

    def post(self, request, product_id, *args, **kwargs):

        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if product_id in list(cart.keys()):
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(redirect_url)
