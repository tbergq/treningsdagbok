# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='max_members',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='valid_to_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 26, 13, 28, 35, 612654, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
