from django.test import TestCase

from products.models import Warehouse


class WarehouseTest(TestCase):

    def test_add_product(self):
        warehouse = Warehouse.objects.create(name="Test")

        self.assertEqual(warehouse.name, "Test")
