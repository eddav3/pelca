# -*- coding: utf-8 -*-
from django.db import models
from brand.models import Brand
from category.models import Category
from pmodel.models import Pmodel

# Create your models here.


class Producto(models.Model):
        ProductName = models.CharField('Nombre de Producto', max_length=30, help_text='Ingrese el nombre del producto')
        Brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
        Description = models.TextField('Descripción', max_length=50, help_text='Ingrese una descripción de este Producto')
        Model = models.ForeignKey(Pmodel, on_delete=models.PROTECT, verbose_name='Modelo')
        Category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
        Price = models.DecimalField('Précio',max_digits=18, decimal_places=2)
        existence = models.FloatField('Existéncia')
        min_existence = models.FloatField('Existéncia_Minima')

        class Meta:
            verbose_name = 'Producto'
            verbose_name_plural = 'Productos'

        def __unicode__(self):
            return '%s %s %s %s' % (self.ProductName, self.Price, self.existence, self.min_existence)
