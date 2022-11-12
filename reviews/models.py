from django.db import models
from django.contrib.auth.models import User
from products.models import AllProducts


# Create your models here.
class ProductReviews(models.Model):
    """"
    Model for reviews
    """

    product = models.ForeignKey(
        AllProducts,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        # editable=False,
        related_name='product_reviewed')
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='review_author')
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    times_updated = models.IntegerField(
        null=False,
        blank=False,
        editable=False,
        default=0
        )
    previous_rating = models.IntegerField(
        null=True,
        blank=True,
        editable=False,
        default=0
        )

    def __str__(self):
        return self.title

    class Meta:
        """"
        Alters the name of the product in the admin panel
        """

        verbose_name_plural = 'Reviews'
        ordering = ['-date']

    def save(self, *args, **kwargs):
        """"
        Override the original save method to increase the
        products accumulated rating and number of reviews
        """
        self.times_updated += 1
        if self.times_updated <= 1:
            self.product.number_of_ratings += 1
            self.product.accumulative_rating += self.rating
            self.previous_rating = self.rating
        else:
            self.product.accumulative_rating -= self.previous_rating
            self.product.accumulative_rating += self.rating
            self.previous_rating = self.rating

        self.product.save()
        super().save(*args, **kwargs)
