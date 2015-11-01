# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0002_musclegroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseexercise',
            name='muscle_group',
            field=models.ForeignKey(to='Program.MuscleGroup'),
        ),
    ]
