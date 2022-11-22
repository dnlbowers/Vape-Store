from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    User Profile Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    default_delivery_name = models.CharField(max_length=254, blank=True)

    default_email = models.EmailField(max_length=254, blank=True)

    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )

    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )

    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )

    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )

    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    default_country = CountryField(
        blank_label="-- Select a Country --",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        pulls email and name from the user model
        on creation if blank
        """
        if self.default_email == "":
            self.default_email = self.user.email

        if self.default_delivery_name == "":
            self.default_delivery_name = self.user.get_full_name()

        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:

        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
