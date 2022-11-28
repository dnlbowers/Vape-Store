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
            brand='test_brand',
            description='test_description',
            accumulative_rating=197,
            number_of_ratings=43,
            stock_level=12,
            rrp=12.99,
            discounted_price=10.99,
            image='test_image',
        )
        self.product_page_response = self.client.get(reverse("products"))
        self.product_detail_response = self.client.get(reverse(
            'product_detail', args=[self.product.slug]
        ))

    def test_products_page_contains_correct_context(self):
        self.assertIn("products", self.product_page_response.context)

    def test_products_details_page_contains_correct_context(self):

        self.assertIn("product", self.product_detail_response.context)

    def test_product_details_come_from_correct_object(self):
        self.assertContains(self.product_detail_response, self.product.name)
        self.assertContains(self.product_detail_response, self.product.sku)
        self.assertContains(
            self.product_detail_response,
            self.product.description)
        self.assertContains(self.product_detail_response, self.product.price)
        self.assertContains(
            self.product_detail_response,
            self.product.current_rating)
        self.assertContains(
            self.product_detail_response,
            self.product.stock_level)
