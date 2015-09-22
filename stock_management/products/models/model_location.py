from django.db import models


class Location(models.Model):

    name = models.CharField(max_length=150)
    warehouse = models.ForeignKey('products.Warehouse')

    def __unicode__(self):
        return u"%s > %s" % (self.warehouse, self.name)
