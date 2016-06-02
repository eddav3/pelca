# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Category(models.Model):
    categoryname = models.CharField('Nombre de Categoria', max_length='30', help_text='Ingrese el Nombre de una categoria')
    description = models.TextField('Descripción', max_length='150',help_text='Ingrese una descripción del prodcuto')

    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
          return '%s %s' % (self.categoryname, self.categoryname)