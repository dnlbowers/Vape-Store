from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View  # noqa
from django.shortcuts import redirect, reverse
from django.contrib import messages
from products.models import AllProducts


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
        product = AllProducts.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if product_id in list(cart.keys()):
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
            messages.success(request, f'You\'ve added {quantity} x {product.name} to your cart')

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(redirect_url)


class EditCartQty(View):
    """"
    View to edit the quantity of a product to the shopping cart
    """

    def post(self, request, product_id, *args, **kwargs):

        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id)

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(reverse('view_cart'))


class RemoveFromCart(View):
    """"
    View to delete a product to the shopping cart
    """

    def post(self, request, product_id, *args, **kwargs):

        cart = request.session.get('cart', {})
        try:
            cart.pop(product_id)
            request.session['cart'] = cart
            return HttpResponse(status=200)

        except Exception as e:
            print(e)
            return HttpResponse(status=500)
