from django.views.generic.base import TemplateView


class ViewShoppingCart(TemplateView):
    """"
    View to render the shopping cart contents
    """
    template_name = 'shopping_cart/cart.html'
