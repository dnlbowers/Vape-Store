from django.contrib import admin
from decimal import Decimal
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter)
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    CategoryGroupings,
    SubCategory,
    Mods,
    PreBuiltCoils,
    AllProducts,
    DisposableVapes,
    Tanks,
    VapeJuice,
    BaseLiquids,
    NicotineShots,
    FlavorConcentrates,
    Batteries,
    Accessories,
    BaseLiquids)


def start_sale(self, request, selected_products):
    """"
    Call back function to start a sale in when called from the admin panel
    created to avoid having to manually change the has_sale boolean of
    each product
    """

    selected_products.update(has_sale=True)
    for product in selected_products:
        product.price = product.discounted_price
        product.save()


def end_sale(self, request, selected_products):
    """"
    Call back function to end a sale in when called from the admin panel
    created to avoid having to manually change the has_sale boolean of
    each product
    """

    selected_products.update(has_sale=False)
    for product in selected_products:
        product.price = product.rrp
        product.save()


def reduce_price_by_10_percent(self, request, selected_products):
    """"
    Call back function to reducred the selected products sale by 10%
    of the RRP so mass sales can be done
    """

    for product in selected_products:
        discounted_price = round(Decimal(product.rrp) * Decimal(0.9), 2)
        product.discounted_price = discounted_price
        product.save()


def reduce_price_by_20_percent(self, request, selected_products):
    """"
    Call back function to reducred the selected products sale by 20%
    of the RRP so mass sales can be done
    """

    for product in selected_products:
        discounted_price = round(Decimal(product.rrp) * Decimal(0.8), 2)
        product.discounted_price = discounted_price
        product.save()


def reduce_price_by_30_percent(self, request, selected_products):
    """"
    Call back function to reduce the selected products sale by 30%
    of the RRP so mass sales can be done
    """

    for product in selected_products:
        discounted_price = round(Decimal(product.rrp) * Decimal(0.7), 2)
        product.discounted_price = discounted_price
        product.save()


def reduce_price_by_40_percent(self, request, selected_products):
    """"
    Call back function to reduce the selected products sale by 40%
    of the RRP so mass sales can be done
    """

    for product in selected_products:
        discounted_price = round(Decimal(product.rrp) * Decimal(0.6), 2)
        product.discounted_price = discounted_price
        product.save()


def reduce_price_by_50_percent(self, request, selected_products):
    """"
    Call back function to reduce the selected products sale by 40%
    of the RRP so mass sales can be done
    """

    for product in selected_products:
        discounted_price = round(Decimal(product.rrp) * Decimal(0.5), 2)
        product.discounted_price = discounted_price
        product.save()


class ModelAChildAdmin(PolymorphicChildModelAdmin, SummernoteModelAdmin):
    """ Base admin class for all child models """
    base_model = AllProducts


@admin.register(DisposableVapes)
class DisposableVapesAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Disposable Vapes model"""
    base_model = DisposableVapes
    show_in_index = False

    def has_module_permission(self, request):
        return False
    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
        
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(Mods)
class ModsAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Mods model"""
    base_model = Mods
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(Tanks)
class TanksAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Tanks model"""
    base_model = Tanks
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description',)
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(PreBuiltCoils)
class PreBuiltCoilsAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the PreBuiltCoils model"""
    base_model = PreBuiltCoils
    show_in_index = False

    def has_module_permission(self, request):
        return False
    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(Batteries)
class BatteriesAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the Batteries model"""
    base_model = Batteries
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(VapeJuice)
class VapeJuiceAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the VapeJuice model"""
    base_model = VapeJuice
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(BaseLiquids)
class BaseLiquidsAdmin(ModelAChildAdmin):
    """ Admin registration and configuration for the BaseLiquids model"""
    base_model = BaseLiquids
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(NicotineShots)
class NicotineShots(ModelAChildAdmin):
    """ Admin registration and configuration for the BaseLiquids model"""
    base_model = NicotineShots
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(FlavorConcentrates)
class FlavorConcentrates(ModelAChildAdmin):
    """ Admin registration and configuration for the BaseLiquids model"""
    base_model = FlavorConcentrates
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(Accessories)
class AccessoriesAdmin(ModelAChildAdmin):
    """
    Admin registration and configuration for the Accessories model
    """
    base_model = Accessories
    show_in_index = False

    def has_module_permission(self, request):
        return False

    # list_display = (
    #     'sku',
    #     'name',
    #     'category',
    #     'rrp',
    #     'price',
    #     'current_rating',
    #     'has_sale',
    #     'image')
    # search_fields = ('name', 'brand', 'description', 'category__name')
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [
    #     'start_sale',
    #     'remove_sale',
    #     'reduce_by_10_percent',
    #     'reduce_by_20_percent',
    #     'reduce_by_30_percent',
    #     'reduce_by_40_percent',
    #     'reduce_by_50_percent']

    # def start_sale(self, request, queryset):
    #     start_sale(self, request, queryset)

    # def remove_sale(self, request, queryset):
    #     end_sale(self, request, queryset)

    # def reduce_by_10_percent(self, request, queryset):
    #     reduce_price_by_10_percent(self, request, queryset)

    # def reduce_by_20_percent(self, request, queryset):
    #     reduce_price_by_20_percent(self, request, queryset)

    # def reduce_by_30_percent(self, request, queryset):
    #     reduce_price_by_30_percent(self, request, queryset)

    # def reduce_by_40_percent(self, request, queryset):
    #     reduce_price_by_40_percent(self, request, queryset)

    # def reduce_by_50_percent(self, request, queryset):
    #     reduce_price_by_50_percent(self, request, queryset)


@admin.register(AllProducts)
class AllProductsAdmin(PolymorphicParentModelAdmin):
    """ Admin registration and configuration for the Product model"""
    base_model = AllProducts
    child_models = (
        DisposableVapes,
        Mods,
        Tanks,
        VapeJuice,
        BaseLiquids,
        Accessories,
        Batteries,
        PreBuiltCoils)
    summer_fields = ('description',)

    list_display = (
        'id',
        'sku',
        'name',
        'category',
        'rrp',
        'price',
        'current_rating',
        'has_sale',
        'image')

    search_fields = (
        'name',
        'brand',
        'description',
        'sku',
        'sub_category__name',
        'category_groupings__name',
        'category__name',
        )

    list_filter = (
        'category',
        'sub_category',
        'has_sale',
        'current_rating',
        'brand',
        )

    prepopulated_fields = {'slug': ('name',)}

    actions = [
        'start_sale',
        'remove_sale',
        'reduce_by_10_percent',
        'reduce_by_20_percent',
        'reduce_by_30_percent',
        'reduce_by_40_percent',
        'reduce_by_50_percent']

    def start_sale(self, request, queryset):
        start_sale(self, request, queryset)

    def remove_sale(self, request, queryset):
        end_sale(self, request, queryset)

    def reduce_by_10_percent(self, request, queryset):
        reduce_price_by_10_percent(self, request, queryset)

    def reduce_by_20_percent(self, request, queryset):
        reduce_price_by_20_percent(self, request, queryset)

    def reduce_by_30_percent(self, request, queryset):
        reduce_price_by_30_percent(self, request, queryset)

    def reduce_by_40_percent(self, request, queryset):
        reduce_price_by_40_percent(self, request, queryset)

    def reduce_by_50_percent(self, request, queryset):
        reduce_price_by_50_percent(self, request, queryset)


@admin.register(CategoryGroupings)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration for
    the Category groupings model
    """
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """
    Admin registration and configuration
    for the Category groupings model
    """
    list_display = (
        'friendly_name',
        'name',
    )
