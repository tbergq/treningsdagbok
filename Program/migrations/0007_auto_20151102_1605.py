# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0006_auto_20151101_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.DateField(),
        ),
    ]
