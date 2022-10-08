from itertools import product
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Product, DisposableVapes

# Register your models here.


class ModelAChildAdmin(PolymorphicChildModelAdmin, SummernoteModelAdmin):
    """ Base admin class for all child models """
    base_model = Product

@admin.register(DisposableVapes)
class ProductAdmin(ModelAChildAdmin):
    base_model = DisposableVapes
    show_in_index = True

@admin.register(Product)
class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Product
    child_models = (DisposableVapes,)
    summer_fields = ('description',)
    list_display = ('sku', 'name', 'category', 'rrp', 'price', 'current_rating', 'has_sale', 'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        queryset.update(has_sale=True)
        for obj in queryset:
            obj.price = obj.discounted_price
            obj.save()
        

    def remove_sale(self, request, queryset):
        queryset.update(has_sale=False)
        for obj in queryset:
            obj.price = obj.rrp
            obj.save()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'programmatic_name',
        'friendly_name',
    )
