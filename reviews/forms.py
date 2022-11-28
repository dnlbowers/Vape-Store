from .models import ProductReviews
from django.forms import ModelForm


class ProductReviewForm(ModelForm):
    """
    A form to allow users to leave a review
    """

    class Meta:
        model = ProductReviews
        fields = ['title', 'content', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initializes the form attributes
        """

        placeholders = {
            'title': 'Your review in a sentence',
            'content': 'Tell us some more about your experience',
            'rating': 'Enter a rating out of 5',
        }

        self.fields['rating'].widget.attrs['min'] = 1
        self.fields['rating'].widget.attrs['max'] = 5
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = placeholder
            self.fields[field].label = False
