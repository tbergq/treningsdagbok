# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workout', '0002_otheractivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otheractivity',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
