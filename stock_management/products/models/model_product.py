from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150, unique=True)
    barcode = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name, )
