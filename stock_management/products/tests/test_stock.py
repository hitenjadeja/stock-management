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
