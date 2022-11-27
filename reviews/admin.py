from django.contrib import admin
from .models import ProductReviews


@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    """
    Allows staff to view/filter customer reviews
    """
    baseModel = ProductReviews
    list_display = (
        'product',
        'author',
        'title',
        'content',
        'rating',
        'date',
        'times_updated',
        'previous_rating',
    )

    list_filter = ('product', 'author', 'date', 'times_updated')

    ordering = ('-date',)
