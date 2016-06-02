# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.ForeignKey(to='employee.Employee')),
                ('position', models.ForeignKey(to='employee.EmployeePosition')),
            ],
            options={
                'verbose_name': 'Detalle de Puesto',
                'verbose_name_plural': 'Detalles de Puesto',
            },
        ),
    ]
