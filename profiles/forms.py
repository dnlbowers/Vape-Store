from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to take in payment details
    and complete an order
    """
    class Meta:
        model = UserProfile
        fields = (
            'default_delivery_name',
            'default_email',
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_delivery_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': '(int. code) Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State, or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs[
                    'aria-label'] = self.fields[field].label
            else:
                self.fields[field].widget.attrs[
                    'aria-label'] = 'select a country'
            self.fields[field].label = False
