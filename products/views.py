from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic, View  # noqa
from django.contrib import messages
from django.db.models import Q
from .models import AllProducts, CategoryGroupings, SubCategory
from django.db.models.functions import Lower
# from .models import Accessories, AllProducts, BaseLiquids, Batteries
# from .models import DisposableVapes, FlavorConcentrates, Mods, NicotineShots
# from .models import PreBuiltCoils, Tanks, VapeJuice


# Keep til later in case needed
# class ProductGroupsMixin(View):
#     ALL_PRODUCTS = [
#         Accessories,
#         BaseLiquids,
#         Batteries,
#         DisposableVapes,
#         FlavorConcentrates,
#         Mods,
#         NicotineShots,
#         PreBuiltCoils,
#         Tanks,
#         VapeJuice
#     ]
#     product_list = []
#     for product in ALL_PRODUCTS:
#         product_list.append(product.objects.all())

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_list'] = self.product_list
#         return context


class AllProductsView(generic.ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 4
    sort = None
    current_ordering = None
    query = None
    categories = None
    subcategories = None

    def get_ordering(self, *args, **kwargs):

        if self.request.GET.get('ordering'):
            sort_by = self.request.GET['ordering']
            self.sort = sort_by

            if sort_by == 'name':
                sort_by = self.request.GET.get('sort_by', 'name')

            elif sort_by == 'price':
                sort_by = self.request.GET.get('ordering', 'price')

            elif sort_by == 'current_rating':
                sort_by = self.request.GET.get('ordering', 'current_rating')
        else:
            sort_by = 'id'
        return sort_by

    # def get_direction(self, *args, **kwargs):
    #     if self.request.GET.get('direction'):
    #         direction = self.request.GET['direction']
    #         if direction == 'desc':
    #             direction = '-'
    #         else:
    #             direction = ''
    #     else:
    #         direction = ''
    #     return direction

    def get_queryset(self, *args, **kwargs):
        products = super(AllProductsView, self).get_queryset(*args, **kwargs)
        if self.request.GET:
            ordering = self.get_ordering(self)
            # direction = self.get_direction(self)
            self.current_ordering = ordering

            if 'category' in self.request.GET:
                self.categories = self.request.GET['category'].split(',')
                products = products.filter(
                    category__name__in=self.categories).order_by(
                        self.current_ordering)

            if 'subcategory' in self.request.GET:
                self.subcategories = self.request.GET['subcategory'].split(',')
                products = products.filter(
                    sub_category__name__in=self.subcategories).order_by(
                        self.current_ordering)

            if 'q' in self.request.GET:
                self.query = self.request.GET['q']
                if not self.query:
                    messages.error(
                        self.request, "You didn't enter any search criteria!")
                    return redirect(reverse('products'))

                queries = Q(
                    name__icontains=self.query) | Q(
                    description__icontains=self.query)

                products = products.filter(queries).order_by(
                    self.current_ordering)

            return products.order_by(self.current_ordering)
        else:
            return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_ordering'] = self.current_ordering
        context['search_query'] = self.query
        context['current_categories'] = self.categories
        context['current_subcategories'] = self.subcategories
        print(type(context['current_subcategories']))
        return context


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
