from django.shortcuts import render
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm


class ContactUs(SuccessMessageMixin, CreateView):
    """"
    Handles the contact form display and submission
    """
    form_class = ContactForm
    template_name = './contact_form/contact_us.html'
    success_url = reverse_lazy('contact_us')
    success_message = 'Your message has been received.\
         We will get back to you as soon as possible via the provided email.'

    def form_valid(self, form):
        """
        Validates form data

        """

        form.save()
        return super().form_valid(form)
