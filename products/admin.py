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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'programmatic_name',
        'friendly_name',
    )
