from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import generic, View  # noqa
from django.contrib import messages
from django.db.models import Q
from .models import AllProducts
from reviews.models import ProductReviews
from reviews.forms import ProductReviewForm
from .forms import ProductForm


class AllProductsView(generic.ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6
    sort = None
    current_ordering = None
    query = None
    categories = None
    subcategories = None
    product_count = 0
    clearance = None

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
        # context['number_of_products'] = AllProducts.objects.count()
        context['current_ordering'] = self.current_ordering
        context['search_query'] = self.query
        context['current_categories'] = self.categories
        context['current_subcategories'] = self.subcategories
        context['clearance'] = self.clearance
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


class EditExistingProduct(View):
    """"
    View to edit an existing product via a form
    """

    def get(self, request, slug, *args, **kwargs):
        """"
        Returns a single product and it details in a form for editing
        """

        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        individual_product = get_object_or_404(AllProducts, slug=slug)
        slug = individual_product.slug
        form = ProductForm(instance=individual_product)

        context = {
            'product': individual_product,
            'form': form,
        }
        return render(
            request,
            'products/edit-product.html', context)

    def post(self, request, slug, *args, **kwargs):
        """"
        Posts the edited details to the database
        """

        individual_product = get_object_or_404(AllProducts, slug=slug)
        slug = individual_product.slug
        form = ProductForm(request.POST, request.FILES,
                           instance=individual_product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated Successfully!')
            return redirect(reverse('product_detail', args=[slug]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
            return render(
                request,
                'products/edit-product.html', {'form': form})


class DeleteProduct(View):
    """"
    View to delete a product
    """
    @staticmethod
    def get(request, *args, **kwargs):
        """"
        Returns a single product and it details
        """

        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        individual_product = get_object_or_404(
            AllProducts, id=kwargs['product_id'])
        individual_product.delete()
        messages.success(request, 'Product Deleted Successfully!')
        return redirect(reverse('products'))
