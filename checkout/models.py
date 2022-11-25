import uuid
from django.db import models
from django.db.models import Sum
from decimal import Decimal

from django.conf import settings
from django_countries.fields import CountryField

from products.models import AllProducts
from profiles.models import UserProfile


class Order(models.Model):
    """"
    Table to keep a record of all customer orders
    """

    ORDER_STATUS = (
        ('Received', 'Order Received'),
        ('Processing', 'Order Processing'),
        ('Dispatched', 'Order Dispatched'),
        ('On Hold', 'On Hold'),
        ('Extra to be paid', 'Extra to be Paid'),
        ('Pending Partial Refund', 'Pending Partial Refund'),
        ('Cancelled Pending Refund', 'Cancelled Pending Refund'),
        ('Cancelled', 'Cancelled'),
    )

    SHIPPING_METHOD = (
        ('Standard', 'Standard Shipping'),
        ('Registered', 'Registered Shipping'),
        ('Free', 'Free Shipping'),
    )

    order_number = models.CharField(max_length=32, null=False, editable=False)

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    full_name = models.CharField(max_length=50, null=False, blank=False)

    email = models.EmailField(max_length=254, null=False, blank=False)

    phone_number = models.CharField(max_length=20, null=False, blank=False)

    country = CountryField(
        blank_label="--Select a Country-- *",
        null=False,
        blank=False)

    postcode = models.CharField(max_length=20, null=True, blank=True)

    town_or_city = models.CharField(max_length=40, null=False, blank=False)

    street_address1 = models.CharField(max_length=80, null=False, blank=False)

    street_address2 = models.CharField(max_length=80, null=True, blank=True)

    county = models.CharField(max_length=80, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    shipping_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_payment_id = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    shipping_method = models.CharField(
        max_length=20,
        choices=SHIPPING_METHOD,
        null=False,
        blank=False,
        default='Standard'
    )

    order_status = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=ORDER_STATUS,
        default='Received'
    )

    times_viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.order_number

    class Meta:
        ordering = ('-date',)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """"
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        if self.order_total < settings.FREE_SHIPPING_QUALIFIER:

            self.shipping_cost = self.order_total * \
                Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)

            if self.shipping_cost < settings.STANDARD_SHIPPING_MINIMUM:

                self.shipping_cost = Decimal(
                    settings.STANDARD_SHIPPING_MINIMUM)

        else:

            self.shipping_cost = 0
            self.shipping_method = 'free'

        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:

            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)

    def delete(self):
        """
        If order gets deleted all lineitems are deleted first
        and order stock get added back to the product
        """
        for lineitem in self.lineitems.all():

            product = AllProducts.objects.get(id=lineitem.product.id)
            product.stock_level += lineitem.quantity
            product.save()

        super().delete()


class InternalOrderNotes(models.Model):
    """
    Model to store internal notes for orders
"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    notes = models.TextField()

    def __str__(self):
        return f'Internal notes for order {self.order.order_number}'


class OrderLineItem(models.Model):
    """
    Model to store each item type in to order
    """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems')

    product = models.ForeignKey(
        AllProducts,
        null=False,
        blank=False,
        on_delete=models.CASCADE)

    quantity = models.IntegerField(null=False, blank=False, default=0)

    previous_quantity = models.IntegerField(null=True, blank=True, default=0)

    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method of a line item in an order
        and adjust the stock if a qty is adjusted post order.
        """

        updated_product = AllProducts.objects.get(id=self.product_id)

        if self.previous_quantity:

            if self.previous_quantity != self.quantity:

                difference = self.quantity - self.previous_quantity

                if difference > 0:

                    check_stock = updated_product.stock_level - difference

                    if check_stock < 0:
                        # done to ensure a staff member does not add more
                        # stock than is available to an amended order.
                        # admin shows a success message but user manual
                        # will explain why stock is not updated
                        pass

                    else:
                        updated_product.stock_level -= difference
                        updated_product.save()
                        self.lineitem_total = self.product.price * \
                            self.quantity
                        self.previous_quantity = self.quantity
                        super().save(*args, **kwargs)

                elif difference < 0:

                    updated_product.stock_level += abs(difference)
                    updated_product.save()
                    self.lineitem_total = self.product.price * self.quantity
                    self.previous_quantity = self.quantity
                    super().save(*args, **kwargs)
            else:

                self.lineitem_total = self.product.price * self.quantity
                self.previous_quantity = self.quantity
                super().save(*args, **kwargs)
        else:

            self.lineitem_total = self.product.price * self.quantity
            self.previous_quantity = self.quantity
            super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

    def delete(self):
        """
        Override the original delete method to update the order total
        and the product stock level upon line item deletion.
        """
        updated_product = AllProducts.objects.get(id=self.product_id)
        updated_product.stock_level += self.quantity
        updated_product.save()
        self.order.update_total()
        super().delete()
