# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField('Nombre de Marca', max_length=30, )
    Description = models.TextField('Descripción', help_text='Ingrese una descripción de esta marca', max_length=30)

    def __unicode__(self):
        return '%s %s' % (self.name, self.Description)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'