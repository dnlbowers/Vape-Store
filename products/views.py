from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic, View  # noqa
from django.contrib import messages
from django.db.models import Q
from .models import AllProducts
from reviews.models import ProductReviews
from reviews.forms import ProductReviewForm


class AllProductsView(generic.ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 8
    sort = None
    current_ordering = None
    query = None
    categories = None
    subcategories = None
    product_count = 0
    clearnace = None

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

    def get_queryset(self, *args, **kwargs):
        products = super(AllProductsView, self).get_queryset(*args, **kwargs)
        if self.request.GET:
            ordering = self.get_ordering(self)
            # direction = self.get_direction(self)
            self.current_ordering = ordering

            if 'clearance' in self.request.GET:
                products = products.filter(has_sale=True)

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
        context['product_count'] = AllProducts.objects.count()
        context['current_ordering'] = self.current_ordering
        context['search_query'] = self.query
        context['current_categories'] = self.categories
        context['current_subcategories'] = self.subcategories
        context['clearnace'] = self.clearnace
        return context


class ProductDetails(View):
    """"
    View to return a single product
    """

    def get(self, request, slug, *args, **kwargs):
        """"
        Returns a single product and it details
        """

        individual_product = get_object_or_404(AllProducts, slug=slug)
        slug = individual_product.slug
        form = ProductReviewForm()

        reviews = ProductReviews.objects.filter(product=individual_product.id)

        context = {
            'product': individual_product,
            'review_form': form,
            'reviews': reviews,
        }
        return render(
            request,
            'products/product-detail.html', context)
