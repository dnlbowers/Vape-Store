from django.contrib import admin
from .models import ProductReviews


@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
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

    ordering = ('-date',)
