from django.db import models


class Warehouse(models.Model):

    name = models.CharField(max_length=150)

    @property
    def stock(self):
        total_stock = []
        for location in self.location_set.all():
            for stock in location.stock_set.all():
                total_stock.append(stock)

        return total_stock

    def __unicode__(self):
        return u'%s' % (self.name, )
