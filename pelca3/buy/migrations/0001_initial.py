# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_provider_contactphone'),
        ('producto', '0002_auto_20160601_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Fecha de Compra')),
                ('total', models.FloatField(null=True, verbose_name=b'Total de Compra', blank=True)),
                ('provider', models.ForeignKey(to='provider.Provider')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='BuyDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(verbose_name=b'Cantidad')),
                ('subtotal', models.FloatField(verbose_name=b'Subtotal')),
                ('buy', models.ForeignKey(related_name='details', to='buy.Buy')),
                ('product', models.ForeignKey(to='producto.Producto')),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalles de Compra',
            },
        ),
    ]
