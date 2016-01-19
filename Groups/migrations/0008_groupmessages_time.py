# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0007_groupmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessages',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 13, 37, 24, 505446), auto_now_add=True),
            preserve_default=False,
        ),
    ]
