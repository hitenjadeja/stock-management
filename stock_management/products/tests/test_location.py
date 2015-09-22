from django.test import TestCase

from products.models import Location, Warehouse


class LocationTest(TestCase):

    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test")

    def test_add_location(self):
        location = Location.objects.create(
            name="Test",
            warehouse=self.warehouse,
        )

        self.assertEqual(location.name, "Test")
        self.assertEqual(location.warehouse, self.warehouse)

    def test_unicode(self):
        location = Location.objects.create(
            name="Location",
            warehouse=self.warehouse,
        )

        self.assertEquals(str(location), "Test > Location")
