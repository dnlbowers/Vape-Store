from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import ProductReviewForm
from products.models import AllProducts
from django.contrib import messages

# Create your views here.


class CreateReview(View):
    """"
    View to create a review from the product details page
    """

    def get(self, request, product_id):
        product = get_object_or_404(AllProducts, id=product_id)
        form = ProductReviewForm()
        context = {
            'form': form,
            'product': product,
        }
        return render(request, 'products/product_detail.html', context)

    def post(self, request, product_id):
        product = get_object_or_404(AllProducts, id=product_id)
        redirect_url = request.POST.get('redirect_url')
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            messages.success(request, 'Review successfully added!')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Failed to add review. Please ensure the \
                form is valid.')
            return redirect(redirect_url)
