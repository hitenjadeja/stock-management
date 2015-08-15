from django.db.utils import IntegrityError
from django.test import TestCase

from products.models import Product, Stock, Warehouse


class StockTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Product")
        self.warehouse = Warehouse.objects.create(name="Warehouse")

    def test_add_stock(self):
        stock = Stock.objects.create(
            product=self.product,
            warehouse=self.warehouse,
            quantity=1,
        )

        self.assertEqual(stock.product.name, "Product")
        self.assertEqual(stock.warehouse.name, "Warehouse")

    def test_product_warehouse_unique(self):
        Stock.objects.create(
            product=self.product,
            warehouse=self.warehouse,
            quantity=1,
        )

        with self.assertRaises(IntegrityError):
            Stock.objects.create(
                product=self.product,
                warehouse=self.warehouse,
                quantity=1,
            )

    def test_string_representation(self):
        stock = Stock.objects.create(
            product=self.product,
            warehouse=self.warehouse,
            quantity=10,
        )

        self.assertEquals(str(stock), "Warehouse: Product x 10")
