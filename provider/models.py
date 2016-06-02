# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from comon.models import Person
from django.db import models

# Create your models here.

SELECCION_TIPOCLIENTE = (

    ('P', 'Particular'),
    ('E', 'Empresa'),
)


class Provider(models.Model):

    first_name = models.CharField('Nombre', max_length=20, help_text='Ingrese Nombre')
    last_name = models.CharField('Apellido', max_length=20, help_text='Ingrese Aepllido')
    address = models.CharField('Dirección', max_length=50, help_text='Ingrese Dirección')
    nit = models.IntegerField('Nit', help_text='Ingrese Numero De Identificación Tributaria')
    contactphone = models.IntegerField('Telefono',help_text='Ingrese un Telefeono de Contacto' )
    typeprovider = models.CharField('Tipo de Proveedor', max_length=1, choices=SELECCION_TIPOCLIENTE, default='P',
                                                                                     help_text='Seleccione el Tipo de Proveedor')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __unicode__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.typeprovider)
