import uuid

from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django.conf import settings
from django_countries.fields import CountryField

from products.models import AllProducts
# from profiles.models import UserProfile


class Order(models.Model):
    """"
    Table to keep a record of all customer orders
    """

    ORDER_STATUS = (
        ('Received', 'Order Received'),
        ('Processing', 'Order Processing'),
        ('Dispatched', 'Order Dispatched'),
    )

    SHIPPING_METHOD = (
        ('Standard', 'Standard Shipping'),
        ('Registered', 'Registered Shipping'),
        ('Free', 'Free Shipping'),
    )

    order_number = models.CharField(max_length=32, null=False, editable=False)
    # user_profile = models.ForeignKey(
    #     UserProfile,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='orders'
    # )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(
        blank_label="* Select a Country",
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
        max_length=20,
        null=False,
        blank=False,
        choices=ORDER_STATUS,
        default='Received'
    )

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
            # if self.shipping_method == 'standard':

            self.shipping_cost = self.order_total * \
                Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
            if self.shipping_cost < settings.STANDARD_SHIPPING_MINIMUM:
                self.shipping_cost = Decimal(
                    settings.STANDARD_SHIPPING_MINIMUM)
            # elif self.shipping_method == 'registered':
            #     self.shipping_cost = self.order_total * \
            #         settings.REGISTERED_SHIPPING_PERCENTAGE / 100
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

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
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
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
