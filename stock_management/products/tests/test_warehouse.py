from django.test import TestCase

from products.models import Product, Stock, Warehouse


class WarehouseTest(TestCase):

    def setUp(self):
        self.product_1 = Product.objects.create(name="Product 1")
        self.product_2 = Product.objects.create(name="Product 2")
        self.warehouse = Warehouse.objects.create(name="Warehouse")

        self.stock_1 = Stock.objects.create(
            product=self.product_1,
            warehouse=self.warehouse,
            quantity=1,
        )

        self.stock_2 = Stock.objects.create(
            product=self.product_2,
            warehouse=self.warehouse,
            quantity=1,
        )

    def test_add_warehouse(self):
        warehouse = Warehouse.objects.create(name="Test")

        self.assertEqual(warehouse.name, "Test")

    def test_list_warehouse_products(self):
        self.assertListEqual(
            list(self.warehouse.products),
            [self.stock_1, self.stock_2],
        )
