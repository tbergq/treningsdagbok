# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20141124_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayexcersice',
            name='description',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
