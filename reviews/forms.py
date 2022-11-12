from .models import ProductReviews
from django.forms import ModelForm


class ProductReviewForm(ModelForm):
    class Meta:
        model = ProductReviews
        fields = ['title', 'content', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Your review in a sentence',
            'content': 'Tell us some more about your experience',
            'rating': 'Select a rating out of 5',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

            if field == 'rating':
                self.fields[field].widget.attrs[
                    'aria-label'] = 'Select a rating out of 5 (required)'
                self.fields[field].label = 'Select a rating out of 5 '
            else:
                self.fields[field].widget.attrs[
                    'aria-label'] = self.fields[field].label
                self.fields[field].label = False
