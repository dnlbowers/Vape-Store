from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic, View  # noqa
from django.contrib import messages
from django.db.models import Q
# from .models import CategoryGroupings, AllProducts
from .models import Accessories, AllProducts, BaseLiquids, Batteries
from .models import DisposableVapes, FlavorConcentrates, Mods, NicotineShots
from .models import PreBuiltCoils, Tanks, VapeJuice


# Keep til later in case needed
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
    product_list = []
    for product in ALL_PRODUCTS:
        product_list.append(product.objects.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = self.product_list
        return context


class AllProductsView(generic.ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        qs = super(AllProductsView, self).get_queryset(*args, **kwargs)
        # products = super(ProductGroupsMixin, self).get_context_data(**kwargs)

        if 'category' in self.request.GET:
            self.categories = self.request.GET['category'].split(',')
            products = qs.filter(category__name__in=self.categories)
            # self.categories = CategoryGroupings.objects.filter(name__in=self.categories)

            return products

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
            return qs

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
        Returns a single product and it details
        """

        individual_product = get_object_or_404(AllProducts, id=id)

        context = {
            'product': individual_product
        }
        return render(
            request,
            'products/product_detail.html', context)
