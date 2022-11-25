from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ProductReviewForm
from products.models import AllProducts
from django.contrib import messages
from .models import ProductReviews


class CreateReview(LoginRequiredMixin, View):
    """"
    View to create a review from the product details page
    """

    def get(self, request, product_id):

        product = get_object_or_404(AllProducts, id=product_id)
        form = ProductReviewForm()

        context = {
            'review_form': form,
            'product': product,
        }

        return render(request, 'reviews/review-form-page.html', context)

    def post(self, request, product_id):

        product = get_object_or_404(AllProducts, id=product_id)
        redirect_url = request.POST.get('redirect_url')

        if redirect_url != f'/products/{product.slug}/':

            redirect_url = f'/products/{product.slug}/'

        form = ProductReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)
            review.product = product
            review.author = request.user

            review.save()

            messages.success(request, 'Review successfully added!')
            return redirect(redirect_url)

        else:

            messages.error(request, 'Failed to add review. Please ensure \
                the form title is valid and you have entered a rating \
                    as a whole number between 1 and 5 (no decimals).')

            return redirect('add_review', product_id)


class EditReview(LoginRequiredMixin, View):
    """"
    View to edit a review from the product details page
    """

    def get(self, request, product_id, review_id):
        """
        Gets the review form prefilled with the current review
        """

        user = request.user

        review = get_object_or_404(ProductReviews, id=review_id)
        product = get_object_or_404(AllProducts, id=product_id)

        if user == review.author or user.is_superuser:

            form = ProductReviewForm(instance=review)
            edit_review = True

            context = {
                'review_form': form,
                'review': review,
                'product': product,
                'edit_review': edit_review,
                'user': user,
            }

            return render(request, 'reviews/review-form-page.html', context)

        else:

            messages.error(request, 'You do not have permission to edit \
                this review.')

            return redirect('product_detail', product.slug)

    def post(self, request, product_id, review_id):
        """
        Handles the form submission to update the review
        """

        review = get_object_or_404(ProductReviews, id=review_id)
        updated_review = ProductReviewForm(request.POST, instance=review)

        redirect_url = request.POST.get('redirect_url')

        if redirect_url != f'/products/{review.product.slug}/':

            redirect_url = f'/products/{review.product.slug}/'

        form = ProductReviewForm(instance=review)

        if updated_review.is_valid():

            review.save()

            messages.success(request, 'Review successfully updated!')

            return redirect(redirect_url)

        else:

            messages.error(request, 'Failed to update review. Please ensure \
                the form title is valid and you have entered a rating \
                    as a whole number between 1 and 5 (no decimals).')

            return redirect('edit_review', review_id)


class DeleteReview(View):
    """"
    View to delete a review from the product details page
    """

    def post(self, request, product_id, review_id):

        review = get_object_or_404(ProductReviews, id=review_id)

        if not request.user.is_superuser or request.user != review.author:

            messages.error(request, 'Sorry, you don\'t have the required\
                 permissions for this.')

            return redirect(reverse('home'))

        else:

            review = get_object_or_404(ProductReviews, id=review_id)
            redirect_url = request.POST.get('redirect_url')

            if redirect_url != f'/products/{review.product.slug}/':

                redirect_url = f'/products/{review.product.slug}/'

            review.delete()

            messages.success(request, 'Review successfully deleted!')

            return redirect(redirect_url)
