from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestPage(TestCase):

    def test_products_page_template(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")