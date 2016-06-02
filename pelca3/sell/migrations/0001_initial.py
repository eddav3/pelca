# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_remove_employee_imagen'),
        ('customer', '0004_customer_customertype'),
        ('producto', '0002_auto_20160601_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Fecha')),
                ('total', models.FloatField(null=True, verbose_name=b'Total', blank=True)),
                ('customer', models.ForeignKey(verbose_name=b'Cliente', to='customer.Customer')),
                ('employee', models.ForeignKey(verbose_name=b'Empleado', to='employee.Employee')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='SellDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(verbose_name=b'Cantidad')),
                ('subtotal', models.FloatField(verbose_name=b'Subtotal')),
                ('product', models.ForeignKey(to='producto.Producto')),
                ('sell', models.ForeignKey(related_name='details', to='sell.Sell')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalles de Venta',
            },
        ),
    ]
