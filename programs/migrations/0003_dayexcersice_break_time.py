# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20141121_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayexcersice',
            name='break_time',
            field=models.TextField(default=b'2', max_length=10),
            preserve_default=True,
        ),
    ]
