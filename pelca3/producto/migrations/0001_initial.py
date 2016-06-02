# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20160601_1651'),
        ('brand', '0002_auto_20160601_1651'),
        ('pmodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProductName', models.CharField(help_text=b'Ingrese el nombre del producto', max_length=30, verbose_name=b'Nombre de Producto')),
                ('Description', models.TextField(help_text=b'Ingrese una descripci\xc3\xb3n de este Producto', max_length=50, verbose_name=b'Descripci\xc3\xb3n')),
                ('Price', models.DecimalField(verbose_name=b'Pr\xc3\xa9cio', max_digits=18, decimal_places=2)),
                ('existence', models.FloatField(verbose_name=b'Exist\xc3\xa9ncia')),
                ('min_existence', models.FloatField(verbose_name=b'Exist\xc3\xa9ncia_Minima')),
                ('Brand', models.ForeignKey(to='brand.Brand', on_delete=django.db.models.deletion.PROTECT)),
                ('Category', models.ForeignKey(to='category.Category', on_delete=django.db.models.deletion.PROTECT)),
                ('Model', models.ForeignKey(to='pmodel.Pmodel', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
