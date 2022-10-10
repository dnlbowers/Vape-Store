from django.views.generic import ListView
from .models import AllProducts, CategoryGroupings

# Create your views here.
class AllProductsView(ListView):
    """"
    View to return all products
    """
    model = AllProducts
    template_name = 'products/products.html'
    paginate_by = 4  

    def get_context_object_name(self, object_list):
        """"
        Passes the products to the template
        """
        return 'products'
