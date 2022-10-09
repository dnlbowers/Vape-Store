from django.views.generic import ListView
from .models import AllProducts, CategoryGroupings

# Create your views here.
class AllProductsView(ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """"
        Passes the products to the template
        """
        context = super().get_context_data(**kwargs)
        context['products'] = AllProducts.objects.all()
        context['categories'] = CategoryGroupings.objects.all()
        return context