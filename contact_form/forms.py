from .models import CustomerMessages
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget


class ContactForm(ModelForm):
    """
    Form to handle contact form submission
    """
    class Meta:
        model = CustomerMessages
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initialise the form attributes
        """

        placeholders = {
            'name': 'Your name',
            'email': 'Your email address',
            'subject': 'Subject of your message',
            'message': 'Your message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:

            if self.fields[field].required:

                placeholder = f'{placeholders[field]} *'

            else:

                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = placeholder
            self.fields[field].label = False
