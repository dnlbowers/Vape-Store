from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    """"
    View to return index page
    """
    template_name = 'home/index.html'
