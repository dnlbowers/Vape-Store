from django.test import TestCase

# Create your tests here.


class TestPage(TestCase):

    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
