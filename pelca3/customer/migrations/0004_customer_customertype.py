# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_type', '0001_initial'),
        ('customer', '0003_auto_20160526_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customertype',
            field=models.ForeignKey(default=0, verbose_name='Tipo de Cliente', to='customer_type.Customertype'),
            preserve_default=False,
        ),
    ]
