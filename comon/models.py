# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


SELECCION_GENERO = (

    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class Person (models.Model):
    first_name = models.CharField('Nombre', max_length=20, help_text='Ingrese Nombre')
    last_name = models.CharField('Apellido',max_length=20, help_text='Ingrese Aepllido')
    address = models.CharField('Dirección', max_length=50, help_text='Ingrese Dirección')
    birthday = models.DateField('Fecha de Nacimiento', help_text='Ingrese Fecha de Nacimiento')
    nit = models.IntegerField('Nit', help_text='Ingrese Numero De Identificación Tributaria')
    gender = models.CharField('Genero', max_length=1, choices=SELECCION_GENERO, default='M', help_text='Selección de Género')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class META:
        abstract = True

