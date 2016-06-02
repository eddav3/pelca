# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from comon.models import Person
from django import *


class EmployeePosition(models.Model):

    first_name = models.CharField('Nombre del Cargo',max_length=50, help_text='Ingrese el nombre del cargo o puesto a crear')
    salary = models.FloatField('Salario del Puesto', max_length=7, help_text='Ingrese el monto a devengar en este puesto')
    start = models.TimeField('Hora de Entrada', help_text='Ingrese el Horario de inicio de labores de este cargo')
    end = models.TimeField('Hora de Salida', help_text='Ingrese el Horario de fin de labores de este cargo')

    def __unicode__(self):

        return '%s' % self.first_name

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'


class Employee (Person):
    position = models.ForeignKey(EmployeePosition, verbose_name='Puesto/Cargo',
                                                         help_text='Selccioney el Cargo o puesto que el empleado Ocupará')
    phonenumber = models.IntegerField('Número de Contacto',
                                                             help_text='Ingrese un Número para contactar al empleado')

    def salario(self):
        return self.position.salary

    def __unicode__(self):

        return '%s %s' % (self.first_name, self.last_name)

    class Meta:

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class PositionDetail(models.Model):
        position = models.ForeignKey(EmployeePosition)
        employee = models.ForeignKey(Employee)

        def __unicode__(self):
            return '%s %s' % (self.position, self.employee)

        class Meta:
            verbose_name = 'Detalle de Puesto'
            verbose_name_plural = 'Detalles de Puesto'


# Create your models here.


