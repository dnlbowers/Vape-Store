from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import AllProducts, CategoryGroupings, SubCategory


class ProductForm(forms.ModelForm):
    """"
    Form to allow quick editing of products from the
    front end.
    """

    class Meta:
        model = AllProducts
        fields = '__all__'

        widgets = {
            'description': SummernoteWidget(),
            'image': CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """"
        Initialise the form attributes
        """

        # taken from boutique ado walk through to display friendly names
        categories = CategoryGroupings.objects.all()
        sub_categories = SubCategory.objects.all()

        category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories]
        sub_category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in sub_categories]

        self.fields['category'].choices = category_friendly_names
        self.fields['sub_category'].choices = sub_category_friendly_names
        self.fields['rrp'].widget.attrs.update({'class': 'text-uppercase'})
        self.fields['name'].widget.attrs['readonly'] = True

        for field in self.fields:

            if self.fields[field].required:

                placeholder = f'{field} *'

            else:

                placeholder = field

            if field == 'image':

                self.fields[field].label = False

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = placeholder
