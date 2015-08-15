from django.db import models


class Warehouse(models.Model):

    name = models.CharField(max_length=150)

    @property
    def products(self):
        return self.stock_set.all()
