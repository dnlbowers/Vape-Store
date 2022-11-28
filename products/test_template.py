from django.test import TestCase
from django.urls import reverse
from products.models import AllProducts, CategoryGroupings, SubCategory


class TestPage(TestCase):

    def setUp(self):
        self.category = CategoryGroupings.objects.create(
            name='test_category', friendly_name='test_category')
        self.subcategory = SubCategory.objects.create(
            name='test_subcategory')
        self.product = AllProducts.objects.create(
            category=self.category,
            sku='test_sku',
            name='test_name',
            slug='test_slug',
            brand='test_brand',
            description='test_description',
            accumulative_rating=197,
            number_of_ratings=43,
            stock_level=12,
            rrp=12.99,
            discounted_price=10.99,
            image='test_image',
        )

    def test_products_page_template(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_products_details_page_template(self):
        response = self.client.get(reverse(
            "product_detail", args=[
                self.product.slug
            ]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product-detail.html")

    def test_non_existent_product_id_returns_404_template(self):
        response = self.client.get(reverse(
            "product_detail", args=[
                'wrong_slug'
            ]))
        self.assertTemplateUsed(response, "errors/404.html")
