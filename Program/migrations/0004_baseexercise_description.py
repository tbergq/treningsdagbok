# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0003_auto_20151031_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseexercise',
            name='description',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
