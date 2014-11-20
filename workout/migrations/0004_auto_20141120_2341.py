# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_dayregister_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayregister',
            name='end_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
