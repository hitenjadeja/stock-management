from django.db import models


class Stock(models.Model):

    product = models.ForeignKey('products.Product')
    warehouse = models.ForeignKey('products.Warehouse')
    quantity = models.IntegerField()
