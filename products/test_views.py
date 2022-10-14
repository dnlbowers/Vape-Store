from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class TestPage(TestCase):

    def test_products_page_contains_correct_context(self):
        response = self.client.get(reverse("products"))
        self.assertIn("products", response.context)

    def test_products_details_page_contains_correct_context(self):
        response = self.client.get(reverse("product_detail", args=[1]))
        self.assertIn("product", response.context)
