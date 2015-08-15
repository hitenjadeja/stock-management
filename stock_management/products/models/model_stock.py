from django.db import models


class Stock(models.Model):

    product = models.ForeignKey('products.Product')
    warehouse = models.ForeignKey('products.Warehouse')
    quantity = models.IntegerField()

    class Meta:

        unique_together = ('product', 'warehouse')

    def __unicode__(self):
        return u'%s: %s x %s' % (
            self.warehouse,
            self.product,
            self.quantity,
        )
