from django.db import models
from employee.models import Employee
from producto.models import Producto
from customer.models import Customer
from django.db.models import Sum
# Create your models here.


class Sell (models.Model):

    employee = models.ForeignKey(Employee, verbose_name='Empleado')
    customer = models.ForeignKey(Customer, verbose_name='Cliente')
    date = models.DateField('Fecha')
    total = models.FloatField('Total', null=True, blank=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def save(self, *args, **kwargs):
        total = self.details.all().aggregate(Sum('subtotal'))
        self.total = total['subtotal__sum']
        super(Sell, self).save(*args, **kwargs)

    def __unicode__(self):
         return '%s %s %s' % (self.employee, self.date, self.total)


class SellDetail (models.Model):

    sell = models.ForeignKey(Sell, related_name='details')
    product = models.ForeignKey(Producto)
    quantity = models.IntegerField('Cantidad')
    subtotal = models.FloatField()

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'

    def save(self, *args, **kwargs):
        product = Producto.objects.get(id=self.product.id)
        product.existence = product.existence - self.quantity
        product.save()
        self.subtotal = self.product.Price * self.quantity
        print self.subtotal
        super(SellDetail, self).save(*args, **kwargs)

