# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreset',
            name='reset_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 11, 16, 20, 818829)),
            preserve_default=False,
        ),
    ]
