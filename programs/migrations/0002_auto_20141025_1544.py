# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayprogram',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='dayprogram',
            name='user',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.RemoveField(
            model_name='periodprogram',
            name='day_program',
        ),
        migrations.DeleteModel(
            name='DayProgram',
        ),
        migrations.DeleteModel(
            name='PeriodProgram',
        ),
    ]
