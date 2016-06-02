# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_positiondetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='imagen',
            field=models.ImageField(upload_to='photos', verbose_name='Carge La foto del Empleado', blank=True),
        ),
    ]
