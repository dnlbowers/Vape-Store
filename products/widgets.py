from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Taken from Boutique ado walk through/django docs to customize
     the image field on the edit product form
    """

    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = \
        'products/custom_widget_templates/custom_clearable_file_input.html'
