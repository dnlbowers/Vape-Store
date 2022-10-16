from django.db import models
from django.utils.text import slugify
from polymorphic.models import PolymorphicModel


class CategoryGroupings(models.Model):
    """"A model for the category of the product"""

    class Meta:
        """"
        Alters the name of the category in the admin panel
        """

        verbose_name_plural = 'Category Groupings'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Passes the friendly name to the template/admin panel
        """

        return self.friendly_name


class AllProducts(PolymorphicModel):
    """Base model for all products"""

    class Meta:
        """"
        Alters the name of the category in the admin panel
        """

        verbose_name_plural = 'All Products'
        ordering = ['id']

    category = models.ForeignKey(
        'CategoryGroupings',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    current_rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True, default=0
    )
    accumulative_rating = models.IntegerField(null=True, blank=True, default=0)
    Number_of_ratings = models.IntegerField(null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
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
        calculates the overall rating from the total number of rating and the
        accumulative rating
        """

        if self.Number_of_ratings == 0:
            return 0
        else:
            self.current_rating = round(
                self.accumulative_rating / self.Number_of_ratings, 2)
            return self.current_rating

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the price
        according to if it has a sale or not
        """
        self.get_rating()

        if self.stock_level <= 0:
            self.in_stock = False

        self.slug = slugify(self.name)

        if self.has_sale:
            self.price = self.discounted_price
        else:
            self.price = self.rrp

        super().save(*args, **kwargs)


class DisposableVapes(AllProducts):
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

    PRODUCT_TYPE = (
        ('disposable', 'Disposable'),
    )

    battery_size = models.CharField(max_length=254, null=True, blank=True)
    max_puffs = models.CharField(max_length=254, null=True, blank=True)
    flavour = models.CharField(max_length=254, null=True, blank=True)
    nicotine_strength = models.CharField(
        max_length=2, choices=NICOTINE_STRENGTHS, default='0')
    liquid_capacity = models.CharField(max_length=254, null=True, blank=True)
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='disposable')


class Mods(AllProducts):
    """Model for mods"""

    class Meta:
        """"
        Alters the name of the category in the admin panel
        """

        verbose_name_plural = 'Mods'

    PRODUCT_TYPE = (
        ('mod', 'Mod'),
    )

    colour = models.CharField(max_length=254, null=True, blank=True)
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='mod')


class Tanks(AllProducts):
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

    PRODUCT_TYPE = (
        ('tank', 'Tank'),
    )

    capacity = models.CharField(max_length=254, null=True, blank=True)
    tank_type = models.CharField(
        max_length=7,
        choices=TANK_TYPE,
        default='Sub-Ohm')

    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='tank')


class PreBuiltCoils(AllProducts):
    """"
    Model for coils
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Pre-Built Coils'

    COIL_TYPE = (
        ('Mesh', 'Mesh'),
        ('Kanthal', 'Kanthal'),
        ('Nickel', 'Nickel'),
        ('Stainless Steel', 'Stainless Steel'),
    )

    PRODUCT_TYPE = (
        ('coil', 'Coil'),
    )

    coil_type = models.CharField(
        max_length=15,
        choices=COIL_TYPE,
        default='Mesh')
    resistance = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    tank = models.ForeignKey(
        'Tanks',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='coils')
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='coil')


class Batteries(AllProducts):
    """"
    Model for batteries
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Batteries'

    BATTERY_TYPE = (
        ('18650', '18650'),
        ('20700', '20700'),
        ('21700', '21700'),
    )

    PRODUCT_TYPE = (
        ('battery', 'Battery'),
    )

    battery_type = models.CharField(
        max_length=5,
        choices=BATTERY_TYPE,
        default='18650')
    capacity = models.CharField(max_length=254, null=True, blank=True)
    discharge_rate = models.CharField(max_length=254, null=True, blank=True)
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='battery')


class VapeJuice(AllProducts):
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

    PRODUCT_TYPE = (
        ('vapejuice', 'Vape Juice'),
    )

    flavour = models.CharField(max_length=254, null=True, blank=True)
    nicotine_strength = models.CharField(
        max_length=2, choices=NICOTINE_STRENGTHS, default='0')
    size = models.CharField(
        max_length=3, choices=BOTTLE_SIZE, default='10')
    pg_vg_ratio = models.CharField(
        max_length=5, choices=PG_VG_MIX_RATIOS, default='50/50')
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='vapejuice')


class BaseLiquids(AllProducts):
    """"
    Model for base liquids
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Base Liquids'

    BOTTLE_SIZE = (
        ('250', '250ml'),
        ('500', '500ml'),
        ('1000', '1000ml'),
    )

    PG_VG_MIX_RATIOS = (
        ('50/50', '50pg/50vg'),
        ('70/30', '70pg/30vg'),
        ('100/0', '100%pg'),
        ('0/100', '100%vg'),
    )

    PRODUCT_TYPE = (
        ('baseliquid', 'Base Liquid'),
    )

    size = models.CharField(
        max_length=4, choices=BOTTLE_SIZE, default='250')
    pg_vg_ratio = models.CharField(
        max_length=5, choices=PG_VG_MIX_RATIOS, default='50/50')
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='baseliquid')


class NicotineShots(AllProducts):
    """"
    Model for nicotine
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Nicotine'

    BOTTLE_SIZE = (
        ('10', '10ml'),
    )

    NICOTINE_STRENGTHS = (
        ('18', '18mg'),
        ('20', '20mg'),
        ('36', '36mg'),
    )

    NICOTINE_TYPE = (
        ('Nicotine', 'Nicotine'),
        ('Nicotine Salt', 'Nicotine Salt'),
    )

    PRODUCT_TYPE = (
        ('nicotine', 'Nicotine'),
    )

    size = models.CharField(
        max_length=2, choices=BOTTLE_SIZE, default='10')
    nicotine_strength = models.CharField(
        max_length=2, choices=NICOTINE_STRENGTHS, default='18')
    nicotine_type = models.CharField(
        max_length=13, choices=NICOTINE_TYPE, default='Nicotine')
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='nicotine')


class FlavorConcentrates(AllProducts):
    """"
    Model for flavor concentrates
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Flavor Concentrates'

    BOTTLE_SIZE = (
        ('10', '10ml'),
        ('30', '30ml'),
    )

    PRODUCT_TYPE = (
        ('concentrate', 'Flavor Concentrate'),
    )

    size = models.CharField(
        max_length=3, choices=BOTTLE_SIZE, default='10')
    flavour = models.CharField(max_length=254, null=True, blank=True)
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='concentrate')


class Accessories(AllProducts):
    """"
    Model for accessories
    """

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Accessories'

    ACCESSORY_TYPE = (
        ('Wire', 'Wire'),
        ('Wick', 'Wick'),
        ('Chargers', 'Chargers'),
        ('Cases', 'Cases'),
        ('Tools', 'Tools'),
        ('Other', 'Other'),
    )

    PRODUCT_TYPE = (
        ('accessory', 'Accessory'),
    )

    accessory_type = models.CharField(
        max_length=8,
        choices=ACCESSORY_TYPE,
        default='Chargers')
    product_type = models.CharField(
        max_length=30,
        choices=PRODUCT_TYPE,
        default='accessory')
