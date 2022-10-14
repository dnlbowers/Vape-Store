from django.shortcuts import get_object_or_404, render
from django.views import generic, View  # noqa

from .models import Accessories, AllProducts, BaseLiquids, Batteries, DisposableVapes, FlavorConcentrates, Mods, NicotineShots, PreBuiltCoils,  Tanks, VapeJuice

# Create your views here.


class AllProducts(generic.ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    paginate_by = 4

    def get_context_object_name(self, object_list):
        """"
        Changes the name of the object that passes the products to the template
        """
        return 'products'


class ProductDetails(View):
    """"
    View to return a single product
    """
    def get(self, request, id, *args, **kwargs):
        """"
        Returns a single product
        """
        all_products = [
            Accessories,
            BaseLiquids,
            Batteries,
            DisposableVapes,
            FlavorConcentrates,
            Mods,
            NicotineShots,
            PreBuiltCoils,
            Tanks,
            VapeJuice
        ]

        for product in all_products:
            if product.objects.filter(id=id).exists():
                product = get_object_or_404(product, id=id)
                context = {
                    'product': product
                }
                return render(
                    request,
                    'products/product_detail.html', context)

        return render(
            request,
            'products/product_detail.html', {
                'product': 'not found'
                })
