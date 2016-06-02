
from django.db import models
from provider.models import Provider
from producto.models import Producto
from django.db.models import Sum


# Create your models here.


class Buy (models.Model):
    provider = models.ForeignKey (Provider)
    date = models.DateField('Fecha de Compra')
    total = models.FloatField('Total de Compra', null=True, blank=True)

    class Meta:
        app_label = 'buy'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __unicode__(self):
        return '%s %s' % ( self.date, self.total)

    def save(self,*args, **kwargs):
        total = self.details.all().aggregate(Sum('subtotal'))
        self.total = total['subtotal__sum']

        print total
        super(Buy, self).save(*args, **kwargs)


class BuyDetail (models.Model):
    buy = models.ForeignKey (Buy, related_name='details')
    product = models.ForeignKey(Producto)
    quantity = models.IntegerField ('Cantidad')
    subtotal = models.FloatField ('Subtotal')

    class Meta:
        app_label = 'buy'
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'

    def __unicode__(self):
        return '%s %s %s %s' % (self.buy, self.product, self.quantity, self.subtotal)

    def save(self, *args, **kwargs):
        product = Producto.objects.get(id=self.product.id)
        product.existence = product.existence + self.quantity
        product.save()
        self.subtotal = self.product.Price * self.quantity
        super(BuyDetail, self).save(*args, **kwargs)