from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic, View  # noqa
from django.contrib import messages
from django.db.models import Q
from .models import Accessories, AllProducts, BaseLiquids, Batteries
from .models import DisposableVapes, FlavorConcentrates, Mods, NicotineShots
from .models import PreBuiltCoils, Tanks, VapeJuice


class ProductGroupsMixin(View):
    ALL_PRODUCTS = [
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


class AllProductsView(ProductGroupsMixin, generic.ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    paginate_by = 4
    query = None

    def get_queryset(self, *args, **kwargs):
        qs = super(AllProductsView, self).get_queryset(*args, **kwargs)
        if 'q' in self.request.GET:
            self.query = self.request.GET['q']
            if not self.query:
                messages.error(
                    self.request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=self.query) | Q(
                description__icontains=self.query)

            products = qs.filter(queries)
            return products
        else:
            qs = qs.order_by("id")
            return qs

    def get_context_object_name(self, object_list):
        """"
        Changes the name of the object that passes the products to the template
        """       
        
        return 'products'


class ProductDetails(ProductGroupsMixin, View):
    """"
    View to return a single product
    """

    def get(self, request, id, *args, **kwargs):
        """"
        Returns a single product and it details
        """
        # all_products = [
        # ..., add the mixin list back here is needed
        #     FlavorConcentrates,
        # ...,
        # ]

        for product in self.ALL_PRODUCTS:
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
