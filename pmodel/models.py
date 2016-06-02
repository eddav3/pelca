# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Pmodel(models.Model):
    name = models.CharField('Nombre de Modelo', max_length=30, )
    Description = models.TextField('Descripción', help_text='Ingrese una descripción de esta marca', max_length=30)

    def __unicode__(self):
        return '%s %s' % (self.name, self.Description)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'