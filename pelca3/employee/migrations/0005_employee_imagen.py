# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20160531_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='imagen',
            field=models.ImageField(default=0, upload_to='photos', verbose_name='Carge La foto del Empleado'),
            preserve_default=False,
        ),
    ]
