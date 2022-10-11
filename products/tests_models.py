from django.test import TestCase
from products.models import AllProducts, CategoryGroupings

# Create your models here.


class Testmodels(TestCase):

    def setUp(self):
        self.category = CategoryGroupings.objects.create(
            name='test_category', friendly_name='test_category')
        self.product = AllProducts.objects.create(
            category=self.category,
            sku='test_sku',
            name='test_name',
            brand='test_brand',
            description='test_description',
            accumulative_rating=197,
            Number_of_ratings=43,
            stock_level=12,
            rrp=12.99,
            discounted_price=10.99,            
        )

    def test_name_is_copied_into_slug_field_upon_creation(self):
        
        self.assertEqual(self.product.slug, 'test_name')

    def test_rating_is_correctly_calculated_the_average_of_all_ratings(self):
        self.assertEqual(self.product.current_rating, 4.58)

    def test_has_sale_is_false_by_default(self):
        self.assertFalse(self.product.has_sale)

    def test_price_is_correctly_calculated_from_rrp(self):
        self.assertEqual(self.product.price, 12.99)
    
    def test_price_is_correctly_calculated_when_has_sale_equals_true(self):
        self.has_sale=True
        self.product.save()
        self.assertEqual(self.product.price, 12.99)
        

