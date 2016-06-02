from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Customertype (models.Model):

    name = models.CharField('Ingrese Tipo de Cliente',max_length=50)

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Tipo de Cliente'
        verbose_name_plural = 'Tipos de Cliente'
