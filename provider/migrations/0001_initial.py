# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text='Ingrese Nombre', max_length=20, verbose_name='Nombre')),
                ('last_name', models.CharField(help_text='Ingrese Aepllido', max_length=20, verbose_name='Apellido')),
                ('address', models.CharField(help_text='Ingrese Direcci\xf3n', max_length=50, verbose_name='Direcci\xf3n')),
                ('nit', models.IntegerField(help_text='Ingrese Numero De Identificaci\xf3n Tributaria', verbose_name='Nit')),
                ('typeprovider', models.CharField(default='P', help_text='Seleccione el Tipo de Proveedor', max_length=1, verbose_name='Tipo de Proveedor', choices=[('P', 'Particular'), ('E', 'Empresa')])),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
