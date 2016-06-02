# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20160526_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(verbose_name='Puesto/Cargo', to='employee.EmployeePosition', help_text='Selccioney el Cargo o puesto que el empleado Ocupar\xe1'),
        ),
    ]
