from django.db import models


class Stock(models.Model):

    product = models.ForeignKey('products.Product')
    location = models.ForeignKey('products.Location')
    quantity = models.IntegerField()

    class Meta:

        unique_together = ('product', 'location')

    def __unicode__(self):
        return u'%s: %s x %s' % (
            self.location,
            self.product,
            self.quantity,
        )
