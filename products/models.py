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
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    current_rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True, default=0
    )
    accumulative_rating = models.IntegerField(null=True, blank=True, default=0)
    Number_of_ratings = models.IntegerField(null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_level = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    has_sale = models.BooleanField(default=False)
    rrp = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    discounted_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the price
        according to if it has a sale or not
        """
        if self.has_sale:
            self.price = self.discounted_price
        else:
            self.price = self.rrp

        super().save(*args, **kwargs)


class DisposableVapes(Product):
    """Model for disposable vapes"""

    class Meta:
        """"
        Alters the name of the product in the admin panel
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


class Mods(Product):
    """Model for mods"""

    class Meta:
        """"
        Alters the name of the category in the admin panel
        """

        verbose_name_plural = 'Mods'

    colour = models.CharField(max_length=254, null=True, blank=True)


class Tanks(Product):
    """"
    Model for tanks
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Tanks'

    TANK_TYPE = (
        ('Sub-Ohm', 'Sub-Ohm'),
        ('RDTA', 'RDTA'),
        ('RTA', 'RTA'),
        ('Dripper', 'Dripper'),
    )

    capacity = models.CharField(max_length=254, null=True, blank=True)
    tank_type = models.CharField(
        max_length=7,
        choices=TANK_TYPE,
        default='Sub-Ohm')
    coil_type = models.ManyToManyField(
        'Coils',
        blank=True,
        related_name='coils')


class VapeJuice(Product):
    """"
    Model for vape juice
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Vape Juice'

    NICOTINE_STRENGTHS = (
        ('0', '0mg'),
        ('3', '3mg'),
        ('6', '6mg'),
        ('12', '12mg'),
        ('18', '18mg'),
        ('24', '24mg'),
    )

    BOTTLE_SIZE = (
        ('10', '10ml'),
        ('30', '30ml'),
        ('50', '50ml'),
        ('75', '75ml'),
        ('100', '100ml'),
    )

    PG_VG_MIX_RATIOS = (
        ('50/50', '50pg/50vg'),
        ('70/30', '70pg/30vg'),
        ('20/80', '20pg/80vg'),
        ('0/100', '100%vg'),
    )

    flavour = models.CharField(max_length=254, null=True, blank=True)
    nicotine_strength = models.CharField(
        max_length=2, choices=NICOTINE_STRENGTHS, default='0')
    size = models.CharField(
        max_length=2, choices=BOTTLE_SIZE, default='10')
    pg_vg_ratio = models.CharField(
        max_length=5, choices=PG_VG_MIX_RATIOS, default='50/50')
