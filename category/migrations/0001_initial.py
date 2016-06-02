# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryname', models.CharField(help_text=b'Ingrese el Nombre de una categoria', max_length=b'30', verbose_name=b'Nombre de Categoria')),
                ('description', models.TextField(help_text=b'Ingrese una descripci\xc3\xb3n del prodcuto', max_length=b'150', verbose_name=b'Descripci\xc3\xb3n')),
            ],
        ),
    ]
