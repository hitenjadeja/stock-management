from django.test import TestCase

from products.models import Product, Stock, Warehouse, Location


class WarehouseTest(TestCase):

    def setUp(self):
        self.product_1 = Product.objects.create(name="Product 1")
        self.product_2 = Product.objects.create(name="Product 2")
        self.warehouse = Warehouse.objects.create(name="Warehouse")
        self.location = Location.objects.create(name="Location", warehouse=self.warehouse)

        self.stock_1 = Stock.objects.create(
            product=self.product_1,
            location=self.location,
            quantity=1,
        )

        self.stock_2 = Stock.objects.create(
            product=self.product_2,
            location=self.location,
            quantity=1,
        )

    def test_add_warehouse(self):
        warehouse = Warehouse.objects.create(name="Test")

        self.assertEqual(warehouse.name, "Test")

    def test_list_warehouse_stock(self):
        self.assertListEqual(
            list(self.warehouse.stock),
            [self.stock_1, self.stock_2],
        )

    def test_string_representation(self):
        self.assertEquals(str(self.warehouse), "Warehouse")
