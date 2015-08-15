from django.db.utils import IntegrityError
from django.test import TestCase

from products.models import Product


class ProductTest(TestCase):

    def test_add_product(self):
        product = Product.objects.create(name="Test")

        self.assertEqual(product.name, "Test")

    def test_product_name_unique(self):
        Product.objects.create(name="Test")
        self.assertRaises(IntegrityError, Product.objects.create, name="Test")

