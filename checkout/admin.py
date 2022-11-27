from django.contrib import admin
from .models import Order, OrderLineItem, InternalOrderNotes


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows editing of line items in the admin
    """

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    exclude = ('previous_quantity',)


class InternalNotesAdmin(admin.StackedInline):
    """
    Internal notes for orders
    """

    model = InternalOrderNotes
    extra = 1
    readonly_fields = ('date',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,
               InternalNotesAdmin)

    readonly_fields = (
        'order_number', 'date',
        'shipping_cost', 'order_total',
        'grand_total', 'original_cart',
        'stripe_payment_id',
    )

    fields = (
        'order_number', 'date', 'full_name',
        'email', 'phone_number', 'country',
        'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county', 'shipping_cost',
        'order_total', 'grand_total', 'original_cart',
        'order_status', 'shipping_method',
        'stripe_payment_id', 'user_profile',
    )

    list_filter = (
        'order_status', 'date', 'shipping_method',
    )

    list_display = (
        'order_number', 'date', 'full_name',
        'order_total', 'shipping_cost',
        'grand_total', 'order_status',
    )

    search_fields = (
        'order_number', 'date', 'full_name',
        'email', 'phone_number', 'country',
        'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county', 'shipping_cost',
        'order_total', 'grand_total', 'original_cart',
        'order_status', 'shipping_method',
        'stripe_payment_id',
    )

    ordering = ('-date',)

    def get_actions(self, request):
        """
        Removes the option to mass delete orders and thus reducing
        human error. Order can still be deleted individually.
        """

        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
