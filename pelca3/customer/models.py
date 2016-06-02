# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from comon.models import Person
from customer_type.models import Customertype

# Create your models here.

SELECCION_DESCUENTO = (

    ('0.01', 'Minorista'),
    ('0.05', 'Frecuente'),
    ('0.10', 'Mayorista'),
)


class Customer (Person):
    discount = models.CharField('Descuento', max_length=5, choices=SELECCION_DESCUENTO, default='0.01')
    customertype = models.ForeignKey(Customertype, verbose_name='Tipo de Cliente')

    def __unicode__(self):
        return '%s %s' % (self.address, self.discount)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


