# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Marca', to='brand.Brand'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Categor\xc3\xada', to='category.Category'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Modelo', to='pmodel.Pmodel'),
        ),
    ]
