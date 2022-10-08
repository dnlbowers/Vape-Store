from django.db import models
from polymorphic.models import PolymorphicModel


class Category(models.Model):
    """"A model for the category of the product"""

    class Meta:
        """"
        Alters the name of the category in the admin panel
        """

        verbose_name_plural = 'Categories'

    programmatic_name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.programmatic_name

    def get_friendly_name(self):
        """
        Passes the friendly name to the template/admin panel
        """

        return self.friendly_name


class Product(PolymorphicModel):
    """Base model for all products"""
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    current_rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True
    )
    accumulative_rating = models.IntegerField(default=0)
    Number_of_ratings = models.IntegerField(null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_level = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    has_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        """
        calculates the overall rating from the total number of rating and the accumulative rating
        """
    
        if self.Number_of_ratings == 0:
            return 0
        else:
            self.current_rating = self.accumulative_rating / self.Number_of_ratings
            return self.current_rating

        


class DisposableVapes(Product):
    """Model for disposable vapes"""

    class Meta:
        """"
        Alters the name of the category in the admin panel
        """

        verbose_name_plural = 'Disposable Vapes'

    NICOTINE_STRENGTHS = (
        ('0', '0mg'),
        ('10', '10mg'),
        ('20', '20mg'),
    )

    battery_size = models.CharField(max_length=254, null=True, blank=True)
    max_puffs = models.CharField(max_length=254, null=True, blank=True)
    flavour = models.CharField(max_length=254, null=True, blank=True)
    nicotine_strength = models.CharField(
        max_length=2, choices=NICOTINE_STRENGTHS, default='0')
    liquid_capacity = models.CharField(max_length=254, null=True, blank=True)


