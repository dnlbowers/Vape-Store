from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from django_summernote.admin import SummernoteModelAdmin
from .models import CategoryGroupings, Mods, PreBuiltCoils, AllProducts, DisposableVapes, Tanks, VapeJuice, BaseLiquids, NicotineShots, FlavorConcentrates, Batteries, Accessories, BaseLiquids

# if time come back and create promo sale functions i,e 10% off all products


def start_sale(self, request, queryset):
    """"
    Call back function to start a sale in when called from the admin panel
    created to avoid having to manually change the price of each product
    """

    queryset.update(has_sale=True)
    for obj in queryset:
        obj.price = obj.discounted_price
        obj.save()


def end_sale(self, request, queryset):
    queryset.update(has_sale=False)
    for obj in queryset:
        obj.price = obj.rrp
        obj.save()


class ModelAChildAdmin(PolymorphicChildModelAdmin, SummernoteModelAdmin):
    """ Base admin class for all child models """
    base_model = AllProducts


@admin.register(DisposableVapes)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Disposable Vapes model"""
    base_model = DisposableVapes
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(Mods)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Mods model"""
    base_model = Mods
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(Tanks)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Tanks model"""
    base_model = Tanks
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(PreBuiltCoils)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the PreBuiltCoils model"""
    base_model = PreBuiltCoils
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(Batteries)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Batteries model"""
    base_model = Batteries
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(VapeJuice)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the VapeJuice model"""
    base_model = VapeJuice
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(BaseLiquids)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the BaseLiquids model"""
    base_model = BaseLiquids
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(NicotineShots)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the BaseLiquids model"""
    base_model = NicotineShots
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(FlavorConcentrates)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the BaseLiquids model"""
    base_model = FlavorConcentrates
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(Accessories)
class ProductAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Accessories model"""
    base_model = Accessories
    show_in_index = True
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(AllProducts)
class ProductAdmin(PolymorphicParentModelAdmin):
    """ Admin registration and configuration for the Product model"""
    base_model = AllProducts
    child_models = (DisposableVapes, Mods, Tanks, VapeJuice, BaseLiquids, Accessories, Batteries, PreBuiltCoils)
    summer_fields = ('description',)
    list_display = (
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')
    search_fields = ('name', 'brand', 'description', 'category__friendly_name')
    actions = ['add_sale', 'remove_sale']

    def add_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)


@admin.register(CategoryGroupings)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin registration and configuration for the Category groupings model"""
    list_display = (
        'friendly_name',
        'programmatic_name',
    )
