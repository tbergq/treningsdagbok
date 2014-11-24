# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_dayexcersice_break_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='baseexercise',
            unique_together=set([('name', 'muscle_group')]),
        ),
    ]
