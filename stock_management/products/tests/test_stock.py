from django.db.utils import IntegrityError
from django.test import TestCase

from products.models import Product, Stock, Warehouse, Location


class StockTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Product")
        self.warehouse = Warehouse.objects.create(name="Warehouse")
        self.location = Location.objects.create(name="Location", warehouse=self.warehouse)

    def test_add_stock(self):
        stock = Stock.objects.create(
            product=self.product,
            location=self.location,
            quantity=1,
        )

        self.assertEqual(stock.product.name, "Product")
        self.assertEqual(stock.location.warehouse.name, "Warehouse")
        self.assertEqual(stock.location.name, "Location")

    def test_product_warehouse_unique(self):
        Stock.objects.create(
            product=self.product,
            location=self.location,
            quantity=1,
        )

        with self.assertRaises(IntegrityError):
            Stock.objects.create(
                product=self.product,
                location=self.location,
                quantity=1,
            )

    def test_string_representation(self):
        stock = Stock.objects.create(
            product=self.product,
            location=self.location,
            quantity=10,
        )

        self.assertEquals(str(stock), "Warehouse > Location: Product x 10")
