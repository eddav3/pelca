# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pmodel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Nombre de Marca')),
                ('Description', models.TextField(help_text=b'Ingrese una descripci\xc3\xb3n de esta marca', max_length=30, verbose_name=b'Descripci\xc3\xb3n')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
            },
        ),
    ]
