# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='contactphone',
            field=models.IntegerField(default=0, help_text='Ingrese un Telefeono de Contacto', verbose_name='Telefono'),
            preserve_default=False,
        ),
    ]
